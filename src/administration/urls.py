from rest_framework.routers import DefaultRouter

from administration.views import OrganizationViewSet, CategoryViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('organisations', OrganizationViewSet)
router.register('categories', CategoryViewSet)
router.register('user-profiles', UserProfileViewSet)
