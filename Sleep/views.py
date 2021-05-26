from django.views import generic
from django.shortcuts import redirect

from map.models import Sleep

# Create your views here.
class SleepListView(generic.ListView):
    model = Sleep
    paginate_by = 10



class SleepDetailView(generic.DetailView):
    model = Sleep


