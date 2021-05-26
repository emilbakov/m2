from djgeojson.fields import GeometryCollectionField
from django.db import models

from datetime import datetime


# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

# animal model
class Animal(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
   
    
    def __str__(self):
        return self.name 


class HuntingSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = GeometryCollectionField()
    hardurl = models.CharField(blank=True,null=True,max_length=256)
    photo_1 = models.ImageField(blank=True,null=True)
    photo_2 = models.ImageField(blank=True,null=True)
    photo_3 = models.ImageField(blank=True,null=True)
    photo_4 = models.ImageField(blank=True,null=True)
    photo_5 = models.ImageField(blank=True,null=True)
    photo_6 = models.ImageField(blank=True,null=True)
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this huntingspot."""
        return reverse('spot-detail', args=[str(self.id)])

    @property
    def picture_url(self):
        return self.picture.url

# more images for the main model
class SpotImages(models.Model):
    huntingspot = models.ForeignKey(HuntingSpot, related_name='images', default=None , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.huntingspot.title

    @property
    def image_url(self):
        return self.image.url

# for accommodation
class Sleep(models.Model):
    huntingspot = models.ForeignKey(HuntingSpot,related_name='sleeps', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    bedroms = models.IntegerField(blank=True,null=True)
    bathrooms = models.DecimalField( max_digits=2, decimal_places=1,blank=True,null=True)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField(blank=True,null=True)
    lot_size = models.DecimalField(max_digits= 5 ,decimal_places=1)
    photo_main = models.ImageField()
    photo_1 = models.ImageField( blank=True)
    photo_2 = models.ImageField( blank=True)
    photo_3 = models.ImageField( blank=True)
    photo_4 = models.ImageField( blank=True)
    photo_5 = models.ImageField( blank=True)
    photo_6 = models.ImageField( blank=True)
    is_publish = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this huntingspot."""
        return reverse('sleep-detail', args=[str(self.id)])

    @property
    def picture_url(self):
        return self.photo_main.url