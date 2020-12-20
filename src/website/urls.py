from rest_framework.routers import DefaultRouter

from website.views import PartnerViewSet, FaqViewSet, MenuItemViewSet, ArticleViewSet, NewsletterViewSet, WantToHelpViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet)
router.register('faqs', FaqViewSet)
router.register('menu-items', MenuItemViewSet)
router.register('articles', ArticleViewSet)
router.register('newsletter', NewsletterViewSet)
router.register('want-to-help', WantToHelpViewSet)

