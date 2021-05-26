from django.shortcuts import render
from django.views import generic
from map.models import HuntingSpot,Animal

class AnimalView(generic.ListView):
    model = Animal

class AnimalDetailView(generic.DetailView):
    model = Animal

# търсене по вид животно...more work #  
class WolfAnimalView(generic.ListView):
    model = HuntingSpot    
    paginate_by = 10
    

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        object_list = qs.filter(animals__name='вълк')
        
        # filter by a variable captured from url, for example
        return object_list


class DeerAnimalView(generic.ListView):
    model = HuntingSpot    
    paginate_by = 10
    

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        object_list = qs.filter(animals__name='елен')
        
        # filter by a variable captured from url, for example
        return object_list

class BoarAnimalView(generic.ListView):
    model = HuntingSpot    
    paginate_by = 10
    

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        object_list = qs.filter(animals__name='глиган')
        
        # filter by a variable captured from url, for example
        return object_list
        



