from django.contrib import admin
from .models import Category,Product,Supplier

# Register your models here.
@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('name',)}


@admin.register(Supplier)

class SupplierAdmin(admin.ModelAdmin):    
    list_display = ('name', 'email', 'phone_number', 'city')  # Display these fields in the admin list view
    search_fields = ('name',  'phone_number')
