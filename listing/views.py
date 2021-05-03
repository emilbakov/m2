from django.shortcuts import render
from django.views import generic
from map.models import HuntingSpot

# Create your views here.
class SpotListView(generic.ListView):
    model = HuntingSpot    
    paginate_by = 10


class SpotDetailView(generic.DetailView):
    model = HuntingSpot    
    
    

