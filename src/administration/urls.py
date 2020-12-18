from rest_framework.routers import DefaultRouter

from administration.views import FaqViewSet

router = DefaultRouter()
router.register('faqs', FaqViewSet)

