from rest_framework.routers import DefaultRouter

from administration.views import (
    OrganizationViewSet,
    CategoryViewSet,
    OpportunityViewSet,
)

router = DefaultRouter()
router.register("organisations", OrganizationViewSet)
router.register("categories", CategoryViewSet)
router.register("opportunities", OpportunityViewSet)
