#TODO search: is it possible to define how a field in a model should be treated in form or model form ? 
# so, can i set defautl behavior of field track_id so that any form or modelform based on that model
# will display field in specific way ? 

from pyexpat import model
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
    track = models.ForeignKey( "Track", on_delete=models.CASCADE , null=True)
    intake = models.ForeignKey( "Intake", on_delete=models.CASCADE, null=True)




class Track( models.Model ):
    name = models.CharField( max_length= 100 )
    description = models.TextField( max_length = 5000 )
    # TODO investigate how pros and cons of this approach to solve 'foreign key field issue' 
    def __str__(self):
        return '%s' % self.name


class Intake( models.Model ):
    intake_no = models.IntegerField()
    start_date = models.DateField( null = True)
    end_date = models.DateField( null=True)
    def __str__(self):
        return '%s' % self.intake_no
