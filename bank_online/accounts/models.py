from django.db import models

from bankingapp.models import District, Branch


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=124)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender_male = models.CharField(max_length=20, null=True)
    gender_female = models.CharField(max_length=30, null=True)
    age = models.CharField(max_length=3, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    mat = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
