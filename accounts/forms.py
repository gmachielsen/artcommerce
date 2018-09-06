from django import forms
from .models import Buyer, Seller

class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Buyer
        fields=['email']
        
        
class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields=['verified', 'full_name', 'phone_number', 'country', 'Title', 'Company_name', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'KVK_Nummer', 'email'  ]

class CardForm(forms.Form):
    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2036)]
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
