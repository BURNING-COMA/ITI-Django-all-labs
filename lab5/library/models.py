from django.db import models
from django.forms import ModelChoiceField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    bid = models.AutoField(primary_key=True)
    author_id = models.ForeignKey( 'Author', on_delete=models.CASCADE)


class Author( models.Model ):
    first_name = models.CharField( max_length=200 )
    last_name = models.CharField( max_length=200 )
  

     
