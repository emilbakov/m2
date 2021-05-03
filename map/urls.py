from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register('maps', views.HuntingViewSet)


app_name = 'map'

urlpatterns = [
    path('', include(router.urls))
]