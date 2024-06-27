from django.db import models

# Create your models here.

class Eshkhi(models.Model):
    color = models.CharField(max_length=200)
    picture = models.CharField(max_length=300)
    description = models.TextField(max_length=200)
    matter = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.color} _ {self.matter}"

