from django import forms
from .models import Order
from shop.models import Supplier

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['supplier','first_name','last_name','email','address','postal_code','city']
