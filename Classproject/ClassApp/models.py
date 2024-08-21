from django.db import models

# Create your models here.


class Parent(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)

   

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')  
    phone_number = models.IntegerField()
    hobby = models.CharField(max_length=100)

    
