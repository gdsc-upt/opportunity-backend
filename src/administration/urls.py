from rest_framework.routers import DefaultRouter

from administration.views import PartnerViewSet, ExampleModelViewSet, FaqViewSet, ArticleViewSet, OrganizationViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
router.register('example-model', ExampleModelViewSet)
router.register('faqs', FaqViewSet)
router.register('article', ArticleViewSet)
router.register('organisation', OrganizationViewSet)
