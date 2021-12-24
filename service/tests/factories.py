import factory
from service.models import Category, Service, OsPlatform


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Faker('name')


class OsPlatformFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OsPlatform
    name = factory.Faker('name')
    is_free = factory.Faker('boolean')
    description = factory.Faker('sentence')


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service
    name = factory.Faker('name')
    price = factory.Faker('pydecimal', left_digits=1, right_digits=2, positive=True)
    description = factory.Faker('sentence')
    category = factory.SubFactory(CategoryFactory)
