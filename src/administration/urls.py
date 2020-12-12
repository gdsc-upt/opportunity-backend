from rest_framework.routers import DefaultRouter

from administration.views import NewsViewSet

router = DefaultRouter()
router.register('news', NewsViewSet)
