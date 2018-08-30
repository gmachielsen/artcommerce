from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Enter Description")
    
    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    FORMAAT_CHOICES = (
	    ('X', 'Kies formaat'),
        ('G', 'Groot'),
        ('M', 'Medium'),
        ('K', 'Klein'),
    )
    
    ORIËNTATIE_CHOICES = (
	    ('X', 'Kies oriëntatie'),
        ('L', 'Liggend'),
        ('S', 'Staand'),
        ('V', 'Vierkant'),
        ('D', 'Driedimensionaal')
    )
    
    TECHNIEK_CHOICES = (
	    ('X', 'Kies techniek'),
        ('S', 'Sculptuur'),
        ('F', 'Fotografie'),
	    ('D', 'Doek, Paneel'),
        ('P', 'Papier'),
        ('G', 'Grafiek'),
        ('D', 'Digitale techniek'),
        ('O', 'Overig'),
    )

    PRIJS_CHOICES = (
    	('X', 'Kies prijs'),
    	('B', 'Tot 499 euro'),
    	('M', '500 tot 999 euro'),
    	('H', '1000 to 2999 euro'),
    	('L', '3000 euro en hoger')
    )
	
    PRIJSTYPE_CHOICES = (
    	('X', 'Kies prijstype'),
    	('B', 'Geen voorkeur'),	
    	('K', 'Koop'),
    	('H', 'Huur'),
    )

    STIJL_CHOICES = (
    	('X', 'Kies jouw kunststijl'),
    	('R', 'Realistisch'),	
    	('I', 'Imprestionistisch'),
    	('A', 'Abstract'),
    	('E', 'Expressionistisch'),
    	('F', 'Figuratief'),
    )
    
    THEME_CHOICES = (
        ('X', 'Kies jouw thema'),
        ('A', 'Architectuur'),
        ('D', 'Dieren'),
        ('E', 'Eten en Drinken'),
        ('L', 'Landschap en Natuur'),
        ('C', 'Cultuur en Land'),
        ('M', 'Mens en Portret'),
        ('O', 'Overig'),
    )
    
    LIJST_CHOICES = (
        ('L', 'Ja'),
        ('Z', 'Nee'),
    )
 
    name = models.CharField(max_length=100)
    description = models.TextField(default="Enter Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    rent = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='product_images')
    formaat=models.CharField(max_length=1, default= 'X', choices=FORMAAT_CHOICES)
    oriëntatie = models.CharField(max_length=1, default= 'X', choices=ORIËNTATIE_CHOICES)
    techniek = models.CharField(max_length=1, default= 'X', choices=TECHNIEK_CHOICES)
    prijs =models.CharField(max_length=1, default= 'X', choices=PRIJS_CHOICES)  
    prijstype =models.CharField(max_length=1, default= 'X', choices=PRIJSTYPE_CHOICES) 
    stijl =models.CharField(max_length=1, default= 'X', choices=STIJL_CHOICES)
    thema =models.CharField(max_length=1, default= 'X', choices=THEME_CHOICES)
    kunstenaar = models.ForeignKey(Artist, null=False, related_name="artworks", on_delete=models.CASCADE)
    lijst =models.CharField(max_length=1, default= 'X', choices=LIJST_CHOICES)
    

    def __str__(self):
        return self.name
        
        
class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
    image = models.ImageField()
