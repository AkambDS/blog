from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField(blank=False)
    summary = models.TextField()
    featured= models.BooleanField(blank=False,null=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        try:
            return reverse("products:product_search", kwargs={"id": self.id})
        except Exception as err:
            print('some error occured', err)

