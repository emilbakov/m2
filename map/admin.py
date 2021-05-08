from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as hunting_models

from .models import ImageAlbum ,Image




admin.site.register(hunting_models.HuntingSpot, LeafletGeoAdmin)
admin.site.register(ImageAlbum)
admin.site.register(Image)