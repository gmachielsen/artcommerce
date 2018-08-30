from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="buyer")
    phone_number = models.CharField(max_length=20, default="unknown", null=False, blank=False)
    
    def __str__(self):
        return self.user.username
        
        
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    verified = models.BooleanField(default=False)
    joined = models.DateField(auto_now_add=True)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    Title = models.CharField(max_length=20, blank=False)
    Company_name = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    KVK_Nummer = models.CharField(max_length=8, blank=False)
    stripe_id = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return self.user.username
