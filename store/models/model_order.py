from django.db import models
from .model_customer import Customer
from .model_product import Product
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=25, default='')
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.customer
    
