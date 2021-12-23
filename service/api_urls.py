from rest_framework.routers import SimpleRouter

from service.view.views import ServiceViewSet

router = SimpleRouter(trailing_slash=False)

router.register('service', ServiceViewSet, basename='service')

urlpatterns = router.urls
