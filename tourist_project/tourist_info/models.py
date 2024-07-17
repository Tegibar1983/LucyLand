from django.db import models

# Create your models here.

class TouristInfo(models.Model):
<<<<<<< HEAD
    region_number=models.SmallIntegerField()
=======
    region_number=models.PositiveSmallIntegerField()
>>>>>>> 8da5056bc9c0ef8474439e7ec4c9b6cc57e3e5b9
    region_name=models.CharField(max_length=200)
    capital_city=models.CharField(max_length=200)
    map=models.ImageField(upload_to='map')
    telephone=models.PositiveBigIntegerField()
    email=models.EmailField()
    website=models.URLField()
<<<<<<< HEAD
    
=======

    def __str__(self):
        return self.region_name
>>>>>>> 8da5056bc9c0ef8474439e7ec4c9b6cc57e3e5b9
