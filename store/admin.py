from django.contrib import admin
from store.models.model_product import Product
from mptt.admin import MPTTModelAdmin
from store.models.model_category import Category
from store.models.model_customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, MPTTModelAdmin)  
admin.site.register(Customer)
