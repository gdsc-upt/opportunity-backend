from rest_framework.routers import DefaultRouter

from administration.views import OrganizationViewSet,WantToHelpViewSet, OpportunityCatViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('organisation', OrganizationViewSet)
router.register('want-to-help', WantToHelpViewSet)
router.register('opportunity-category', OpportunityCatViewSet)
router.register('user-profile', UserProfileViewSet)
