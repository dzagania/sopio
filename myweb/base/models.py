from django.db import models
from django.contrib.auth.models import AbstractUser


class Style(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class Eshkhi(models.Model):
    style = models.ManyToManyField(Style, blank=True, related_name="eshkhi")
    color = models.CharField(max_length=200)
    picture = models.CharField(max_length=300)
    description = models.TextField(max_length=200)
    matter = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.color} _ {self.matter}"


class User(AbstractUser):
    clothes = models.ManyToManyField(Eshkhi, blank=True, related_name="users")