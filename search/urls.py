from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import url



from django.urls import path
from .views import AnimalView, AnimalDetailView, WolfAnimalView, DeerAnimalView ,BoarAnimalView


urlpatterns = [   
    
    path('animals/', AnimalView.as_view(), name='animal'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('wolf/',WolfAnimalView.as_view(), name='search-wolf'),
    path('deer/',DeerAnimalView.as_view(), name='search-deer'),
   
    path('boar/',BoarAnimalView.as_view(), name='search-boar'),
   
    

    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    