"""darpan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    #path('autocomplete/', include('dal.urls')),
    path('city/', include('cities.urls', namespace='city')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('template', TemplateView.as_view(template_name='template.html')),
    path('admin/', admin.site.urls),

    path('post/', include('posts.urls', namespace='post')),

    path('chart/', include('charts.urls', namespace='chart')),
    path('numerology/', include('numerology.urls', namespace='numerology')),
    path('astro/', include('astrology.urls', namespace='astro')),
    path('hds/', include('hds.urls', namespace='hds')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
