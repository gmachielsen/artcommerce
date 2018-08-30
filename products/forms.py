from django import forms
from .models import Product

class ProductSearchForm(forms.ModelForm):
    
    search=forms.CharField(required=False, label="Search")
    
    class Meta:
        model=Product
        fields=['search', 'formaat' ,'oriëntatie' ,'techniek' ,'prijs' ,'prijstype' ,'stijl', 'kunstenaar', 'thema']
        
        