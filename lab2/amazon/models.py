from django.db import models
from django.forms import CharField, EmailField

# Create your models here.

class MyUser( models.Model ):
    user_name = models.CharField( max_length=40, primary_key=True )
    password = models.CharField( max_length=100 )

class Student( models.Model ):
    name = models.CharField( max_length=100 )
    age = models.IntegerField()
    notes = models.CharField( null=True, max_length=1000 )
