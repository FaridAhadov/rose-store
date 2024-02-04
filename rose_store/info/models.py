from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=32)
    map_longitude = models.CharField(max_length=32)
    map_latitude = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.name}"
    
