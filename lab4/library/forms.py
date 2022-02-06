from imp import is_frozen
from django import forms 

class AddBookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    is_free = forms.BooleanField(label='Is Free')
    date_published = forms.DateField(label='Date Published')
    