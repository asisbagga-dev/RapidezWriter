from django import forms
from .models import Database, Category

class Databaseform(forms.ModelForm):
    class Meta:
        model = Database
        fields = ('heading',
                  'description',
                  'banner',
                  'category')


class Categoryform(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
