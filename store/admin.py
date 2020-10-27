from django.contrib import admin
from store.models.model_product import Product
from mptt.admin import MPTTModelAdmin
from store.models.model_category import Category
from store.models.model_customer import Customer
from store.models.model_order import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date']

class AdminOoder(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'status']
admin.site.register(Product, AdminProduct)
admin.site.register(Category, MPTTModelAdmin)  
admin.site.register(Customer)
admin.site.register(Order, AdminOoder)
