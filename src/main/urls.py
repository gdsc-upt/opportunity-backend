from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from administration.urls import router as admin_router
from administration.views import CustomAuthToken, CreateUserView
from website.urls import router as website_router
from common.admin_site import admin_site


urlpatterns = [
    path('', RedirectView.as_view(url='/api/admin/')),
    path('', include('pwa.urls')),
    path('api/admin/', admin_site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/', include(admin_router.urls)),
    path('api/', include(website_router.urls)),
    path('api/auth/token/', CustomAuthToken.as_view()),
    path('api/auth/register/', CreateUserView.as_view())
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('api/__debug__/', include(debug_toolbar.urls), name='debug')]
