from django.db import models

# Create your models here.
class Restaurants(models.Model):
    title = models.CharField(max_length=50, null=False)
    restaurantType = models.CharField(max_length=50, null=True)
    openclose = models.CharField(max_length=50, null=True)
    content = models.TextField()
    rimg = models.ImageField(max_length=250)
    slug = models.CharField(max_length=130, null=True)
    timeStamp = models.DateTimeField()
    
def __str__(self):
    return self.title 
