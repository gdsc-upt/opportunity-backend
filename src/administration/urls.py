from rest_framework.routers import DefaultRouter

from administration.views import OrganizationViewSet

router = DefaultRouter()
router.register('organization', OrganizationViewSet)
