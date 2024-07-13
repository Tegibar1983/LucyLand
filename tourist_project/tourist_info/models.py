from django.db import models

# Create your models here.

class TouristInfo(models.Model):
    region_number=models.PositiveSmallIntegerField()
    region_name=models.CharField(max_length=200)
    capital_city=models.CharField(max_length=200)
    map=models.ImageField(upload_to='map')
    telephone=models.PositiveBigIntegerField()
    email=models.EmailField()
    website=models.URLField()

    def __str__(self):
        return self.region_name
