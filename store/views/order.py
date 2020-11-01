from django.shortcuts import render, redirect
from django.views import View
from store.models.model_product import Product
from store.models.model_order import Order
from store.models.model_customer import Customer
from django.utils.decorators import method_decorator

from store.middlewares.auth import auth_middleware

class OrderView(View):
    @method_decorator(auth_middleware)  
    def get(self, request, *args, **kwargs):
        customer = request.session.get('customer_id')
        orders = Order.get_order_by_customer_id(customer)
        orders = orders.reverse()
        return render(request, 'orders.html',{'orders':orders})