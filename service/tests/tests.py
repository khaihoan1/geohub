from django.test import TestCase

from service.tests.factories import CategoryFactory, OsPlatformFactory, ServiceFactory


class ServiceViewSetTestCase(TestCase):
    base_url = '/service'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = CategoryFactory()
        cls.service_1 = ServiceFactory(category=cls.category)
        cls.service_2 = ServiceFactory()
        cls.os_platform_1 = OsPlatformFactory()
        cls.os_platform_2 = OsPlatformFactory()
        cls.service_1.os_platform.add(cls.os_platform_1, cls.os_platform_2)
        cls.service_1.save()

    def test_get_list(self):
        response = self.client.get(self.base_url)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(2, len(data))
        self.assertEqual(self.service_1.name, data[0]['name'])

    def test_get_list__filter_by_category(self):
        url = self.base_url + f'?category={self.category.name}'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(1, len(data))
        self.assertEqual(self.service_1.name, data[0]['name'])

    def test_get_list__filter_by_os_platforms(self):
        url = self.base_url + f'?os_platform={self.os_platform_1.name},{self.os_platform_2.name}'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(1, len(data))
        self.assertEqual(self.service_1.name, data[0]['name'])

    def test_search_by_name(self):
        url = self.base_url + f'?search={self.service_2.name}'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(1, len(data))
        self.assertEqual(self.service_2.name, data[0]['name'])
