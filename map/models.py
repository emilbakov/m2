from djgeojson.fields import GeometryCollectionField
from django.db import models

# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

class HuntingSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = GeometryCollectionField()
    hardurl = models.CharField(blank=True,null=True,max_length=256)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this huntingspot."""
        return reverse('spot-detail', args=[str(self.id)])

    @property
    def picture_url(self):
        return self.picture.url

    
    

# Create your models here.
