from djgeojson.fields import GeometryCollectionField
from django.db import models

# Used to generate URLs by reversing the URL patterns
from django.urls import reverse

def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'

class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
        
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)


class HuntingSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = GeometryCollectionField()
    hardurl = models.CharField(blank=True,null=True,max_length=256)
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE, blank=True,null=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this huntingspot."""
        return reverse('spot-detail', args=[str(self.id)])

    @property
    def picture_url(self):
        return self.picture.url

    

# Create your models here.
