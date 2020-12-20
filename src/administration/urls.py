from rest_framework.routers import DefaultRouter

from administration.views import PartnerViewSet, ExampleModelViewSet, FaqViewSet, OrganizationViewSet, MenuItemViewSet, \
    ArticleViewSet, \
    NewsletterViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
router.register('example-model', ExampleModelViewSet)
router.register('faqs', FaqViewSet)
router.register('organisation', OrganizationViewSet)
router.register('menu-items', MenuItemViewSet)
router.register('article', ArticleViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('user-profile', UserProfileViewSet)
