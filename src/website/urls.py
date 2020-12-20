from rest_framework.routers import DefaultRouter

from website.views import PartnerViewSet, FaqViewSet, MenuItemViewSet, ArticleViewSet, NewsletterViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
router.register('faqs', FaqViewSet)
router.register('menu-items', MenuItemViewSet)
router.register('article', ArticleViewSet)
router.register('newsletter', NewsletterViewSet)
