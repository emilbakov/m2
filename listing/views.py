
from django.shortcuts import render, get_object_or_404

from django.views import generic
from map.models import HuntingSpot, SpotImages
# Create your views here.

    
class SpotListView(generic.ListView):
    model = HuntingSpot    
    paginate_by = 10



class SpotDetailView(generic.DetailView):
    model = HuntingSpot
    

    def get_context_data(self, **kwargs):
        context = super(SpotDetailView, self).get_context_data(**kwargs)
        

        
        
        print(context)
        
        return context 

 
def detail_view(request, id):
    spot=get_object_or_404(HuntingSpot, id=id)
    photos = SpotImages.objects.filter(spot=spot)
    context = {
        'spot':spot,
        'photos':photos
    }
    return render(request,'detail.html', context)

