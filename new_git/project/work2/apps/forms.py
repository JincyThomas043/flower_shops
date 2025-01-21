from django import forms
from .models import *

class edit_image(forms.ModelForm):
    class Meta:
        model=Productdetails
        fields =[ 'product_name','product_price','description','product_image','category','product_stock']
