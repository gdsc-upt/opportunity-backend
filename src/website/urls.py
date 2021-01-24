from rest_framework.routers import DefaultRouter

from website.views import (
    MenuItemViewSet,
    NewsletterViewSet,
    WantToHelpViewSet,
    ContactViewSet,
    SettingViewSet,
)

router = DefaultRouter()
router.register("menu-items", MenuItemViewSet)
router.register("newsletter", NewsletterViewSet)
router.register("want-to-help", WantToHelpViewSet)
router.register("contact", ContactViewSet)
router.register("settings", SettingViewSet)
