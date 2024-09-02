from django.db import models

# Create your models here.
class Emp(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    def __str__(self):
        return self.name 
class Fm(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    def __str__(self):
        return self.name    
