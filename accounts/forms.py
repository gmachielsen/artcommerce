from django import forms
from .models import Buyer, Seller

class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Buyer
        fields=['phone_number']
        
        
class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields=['verified', 'full_name', 'phone_number', 'country', 'Title', 'Company_name', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'KVK_Nummer'  ]
        
     