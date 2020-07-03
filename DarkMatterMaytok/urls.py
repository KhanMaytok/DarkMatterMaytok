"""DarkMatterMaytok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

from core.views import logout

schema_view = get_schema_view(
    openapi.Info(
        title="MaytokVerso API",
        default_version='v1',
        description="Accede a la materia oscura del Universo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@maytok.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', RedirectView.as_view(url='https://www.youtube.com/watch?v=bR-s4ReIxJo', permanent=False)),
    path('the-forge/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('privacidad/', TemplateView.as_view(template_name='core/privacy.html')),
    path('logout/', logout, name='logout'),
    path('payments/', include('payments.urls')),
    path('', include('blog.urls')),
    path('', include('books.urls')),
    path('comments/', include('django_comments_xtd.urls')),

    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
