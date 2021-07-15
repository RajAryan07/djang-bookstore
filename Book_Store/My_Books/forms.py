from django import forms
from My_Books.models import Form



class UserForm(forms.ModelForm):
    class Meta():
        model = Form
        fields = ['book_name','author_name','genre','language',]
