from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.conf.urls import url



from django.urls import path
from . import views

urlpatterns = [   
    path('', views.SpotListView.as_view(), name='spots'),
    path('spot/<int:pk>/', views.SpotDetailView.as_view(), name='spot-detail'),

    path('map/', TemplateView.as_view(template_name='map.html'), name='map'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)