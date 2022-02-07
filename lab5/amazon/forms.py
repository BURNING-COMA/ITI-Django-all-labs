# TODO find a way to customize how foriegn key field is display to show track name instead of object track x 


from cProfile import label
from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms 

from . import models



class Login( forms.Form ):
    user_name = forms.CharField( max_length=100, )
    password = forms.CharField(widget=forms.PasswordInput)


class Register( forms.Form ):
    user_name = forms.CharField( max_length=100, )
    password = forms.CharField(widget=forms.PasswordInput)


# class Insert( forms.Form ):
#     name = forms.CharField(label='st name', max_length=100 )
#     age = forms.IntegerField()
#     notes = forms.CharField( max_length=1000 )
# FIXME find a way to display track and intake names in update and insert forms .. 
class Insert( forms.ModelForm ):
    # add additional fields besides model fields
    # track = forms.ChoiceField( choices=[(t.id, t.name) for t in models.Track.objects.all()])
    # intake = forms.ChoiceField(choices=[(t.id, t.intake_no) for t in models.Intake.objects.all()])
    class Meta: 
        fields = '__all__'
        model = models.Student
        # widgets = {
        #     'track': forms.Select( attrs={'type': 'text', 'name': 'name', 'placeholder': 'track:'}),
        #     'intake': forms.Select(attrs={'type': 'text', 'name': 'intake_no', 'placeholder': 'intake:'})
        # }
        

    # widgets = {
    #     'invoice_name': forms.TextInput(attrs={'type': 'text', 'name': 'name', 'placeholder': 'Invoice Name:'}),
    #     'organization': forms.Select(attrs={'type': 'text', 'name': 'name', 'placeholder': 'Company:'}),
    #     'items': forms.TextInput(attrs={'type': 'text', 'name': 'name', 'placeholder': 'Items:'}),
    # }
# class Update( forms.Form ):
#     name = forms.CharField( max_length=100 )
#     new_name = forms.CharField( max_length=100 )
#     new_age = forms.IntegerField()
#     new_notes = forms.CharField( max_length=1000)

class Update( forms.ModelForm ):
    student_id = forms.IntegerField( label='Update student with ID')
    class Meta: 
        fields = '__all__'
        model = models.Student

class Delete( forms.Form ):
    student_id = forms.IntegerField()

class Search( forms.Form ):
     name = forms.CharField( max_length=100 )

