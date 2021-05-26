from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as hunting_models
from .models import HuntingSpot,SpotImages,Sleep,Animal

class SpotImageAdmin(admin.StackedInline):
    model= SpotImages

class SpotAdmin(admin.ModelAdmin):
    inlines = [SpotImageAdmin]

    class Meta:
        model= HuntingSpot
class SpotImageAdmin(admin.ModelAdmin):
    pass        





admin.site.register(hunting_models.HuntingSpot, LeafletGeoAdmin)
admin.site.register(SpotImages)
admin.site.register(Sleep)
admin.site.register(Animal)
