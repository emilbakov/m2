from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as hunting_models




admin.site.register(hunting_models.HuntingSpot, LeafletGeoAdmin)