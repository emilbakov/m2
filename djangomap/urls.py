"""djangomap URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from djangomap.view import ContactFormView
from map.models import HuntingSpot
from django.urls import path, include


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('listing/', include('listing.urls')),
    

    url('contact/', ContactFormView.as_view(), name='contact'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    
    
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=HuntingSpot, properties=('title', 'description', 'picture_url','hardurl')), name='data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)