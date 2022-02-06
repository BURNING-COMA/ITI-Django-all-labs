from cProfile import label
from django import forms 

class Login( forms.Form ):
    user_name = forms.CharField( max_length=100, )
    password = forms.CharField(widget=forms.PasswordInput)


class Register( forms.Form ):
    user_name = forms.CharField( max_length=100, )
    password = forms.CharField(widget=forms.PasswordInput)


class Insert( forms.Form ):
    name = forms.CharField( max_length=100 )
    age = forms.IntegerField()
    notes = forms.CharField( max_length=1000 )

class Update( forms.Form ):
    name = forms.CharField( max_length=100 )
    new_name = forms.CharField( max_length=100 )
    new_age = forms.IntegerField()
    new_notes = forms.CharField( max_length=1000)

class Delete( forms.Form ):
    name = forms.CharField( max_length=100 )

class Search( forms.Form ):
     name = forms.CharField( max_length=100 )

