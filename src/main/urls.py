"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from administration.urls import router as admin_router
from website.urls import router as website_router
from common.admin_site import admin_site

schema_view = get_schema_view(
    openapi.Info(
        title="Opportunity API",
        default_version='v1',
        description="Opportunity API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dsc.upt@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/admin/')),
    path('', include('pwa.urls')),
    path('api/admin/', admin_site.urls),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('api/', include(admin_router.urls)),
    path('api/', include(website_router.urls)),
    path('api/auth/token/', obtain_auth_token, name='api_token_auth')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
