from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    #override field def
    title= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))
    class Meta:
        model= Product
        fields= [
            'title','description','price','featured'
        ]


class RawProductForm(forms.Form):
    title= forms.CharField()
    description= forms.CharField()
    price = forms.DecimalField()
    featured= forms.BooleanField()