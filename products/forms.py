from django import forms
from .models import Product

class ProductSearchForm(forms.ModelForm):
    search=forms.CharField(required=False, label="Search")
    class Meta:
        model=Product
        fields=['search', 'formaat' ,'oriëntatie' ,'techniek' ,'prijs' ,'prijstype' ,'stijl', 'kunstenaar', 'thema']

class ProductSellerForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'description', 'price', 'rent', 'lengthcm', 'widthcm', 'image', 'formaat', 'oriëntatie', 'techniek', 'prijs', 'prijstype', 'stijl', 'thema', 'kunstenaar', 'lijst']
     
    
  
        