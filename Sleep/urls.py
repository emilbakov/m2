from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url



from django.urls import path
from .views import SleepListView,SleepDetailView


urlpatterns = [   
    
    path('',SleepListView.as_view(), name='sleep'),
    path('<int:pk>/',SleepDetailView.as_view(), name='sleep-detail'),
    

    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)