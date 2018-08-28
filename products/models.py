from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    FORMAAT_CHOICES = (
	    ('X', 'Kies formaat'),
        ('L', 'Groot'),
        ('M', 'Medium'),
        ('S', 'Klein'),
    )
    
    ORIËNTATIE_CHOICES = (
	    ('X', 'Kies oriëntatie'),
        ('L', 'Liggend'),
        ('S', 'Staand'),
        ('V', 'Vierkant'),
    )
    
    TECHNIEK_CHOICES = (
	    ('X', 'Kies techniek'),
        ('S', 'Sculptuur'),
        ('F', 'Fotografie'),
	    ('D', 'Doek'),
        ('P', 'Papier'),	
    )

    PRIJS_CHOICES = (
    	('X', 'Kies prijs'),
    	('M', '500 tot 3000 euro'),
    	('H', 'Vanaf 3000 euro'),
    	('B', 'Tot 499 euro'),
    )
	
    PRIJSTYPE_CHOICES = (
    	('X', 'Kies prijstype'),
    	('B', 'Koop en Huur'),	
    	('K', 'Koop'),
    	('H', 'Huur'),
    )

    STIJL_CHOICES = (
    	('X', 'Kies jouw kunststijl'),
    	('R', 'Realistisch'),	
    	('I', 'Imprestionistisch'),
    	('A', 'Abstract'),
    	('E', 'Expressionistisch')
    )
    
    
    name = models.CharField(max_length=100)
    description = models.TextField(default="Enter Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    rent = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='product_images')
    formaat =models.CharField(max_length=1, default= 'X', choices=FORMAAT_CHOICES)
    oriëntatie = models.CharField(max_length=1, default= 'X', choices=ORIËNTATIE_CHOICES)
    techniek = models.CharField(max_length=1, default= 'X', choices=TECHNIEK_CHOICES)
    prijs =models.CharField(max_length=1, default= 'X', choices=PRIJS_CHOICES)  
    prijstype =models.CharField(max_length=1, default= 'X', choices=PRIJSTYPE_CHOICES) 
    stijl =models.CharField(max_length=1, default= 'X', choices=STIJL_CHOICES)