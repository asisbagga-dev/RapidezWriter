from django import forms
from .models import Database

class Databaseform(forms.ModelForm):

    class Meta:
        model = Database
        fields = '__all__'
