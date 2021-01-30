from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from administration.urls import router as admin_router
from website.urls import router as website_router
from common.admin_site import admin_site

urlpatterns = [
    path("", RedirectView.as_view(url="/api/admin/")),
    path("", include("pwa.urls")),
    path("api/admin/", admin_site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/", include(admin_router.urls)),
    path("api/", include(website_router.urls)),
    # these 2 are necessary because django allauth tries accesing them using reverse url's
    path("dummy/", TemplateView.as_view(), name="account_email_verification_sent"),
    path(
        "api/auth/password/reset/confirm/<slug:uidb64>/<slug:token>/",
        TemplateView.as_view(),
        name="password_reset_confirm",
    ),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("api/__debug__/", include(debug_toolbar.urls), name="debug")]
