from rest_framework.routers import DefaultRouter
from administration.views import NewsViewSet

from administration.views import PartnerViewSet, ExampleModelViewSet, FaqViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
router.register('example-model', ExampleModelViewSet)
router.register('faqs', FaqViewSet)
router.register('news', NewsViewSet)
