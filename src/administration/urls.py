from rest_framework.routers import DefaultRouter

from administration.views import OrganizationViewSet, CategoryViewSet, UserProfileViewSet, OpportunityViewSet

router = DefaultRouter()
router.register('organisations', OrganizationViewSet)
router.register('categories', CategoryViewSet)
router.register('opportunities', OpportunityViewSet)
router.register('user-profiles', UserProfileViewSet)
