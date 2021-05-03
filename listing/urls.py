from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from . import views

urlpatterns = [   
    path('', views.SpotListView.as_view(), name='spots'),
    path('spot/<int:pk>/', views.SpotDetailView.as_view(), name='spot-detail'),     
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)