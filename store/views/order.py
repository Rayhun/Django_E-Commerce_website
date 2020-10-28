from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from store.models.model_product import Product
from store.models.model_order import Order
from store.models.model_customer import Customer
from django.utils.decorators import method_decorator

from store.middlewares.auth import auth_middleware

class OrderView(View):
    # template_name = "orders.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     customer = self.request.session.get('customer_id')
    #     context['orders'] = Order.get_order_by_customer_id(customer)
    #     return context
    @method_decorator(auth_middleware)  
    def get(self, request, *args, **kwargs):
        customer = request.session.get('customer_id')
        orders = Order.get_order_by_customer_id(customer)
        orders = orders.reverse()
        return render(request, 'orders.html',{'orders':orders})