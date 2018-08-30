from django.contrib import admin
from .models import Product, Artist, ProductImages
# Register your models here.
admin.site.register(Artist)




class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 3
class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]
admin.site.register(Product, ProductAdmin)
