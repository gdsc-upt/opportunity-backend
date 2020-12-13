from rest_framework.routers import DefaultRouter

from administration.views import PartnerViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
