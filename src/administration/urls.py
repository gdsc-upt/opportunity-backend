from rest_framework.routers import DefaultRouter

from administration.views import MenuItemViewSet

router = DefaultRouter()
router.register('menuItems', MenuItemViewSet)
