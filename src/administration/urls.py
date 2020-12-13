from rest_framework.routers import DefaultRouter

from administration.views import PartnerViewSet, ExampleModelViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
router.register('example-model', ExampleModelViewSet)
