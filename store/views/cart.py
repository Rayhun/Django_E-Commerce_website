from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from django.utils.decorators import method_decorator

from store.middlewares.auth import auth_middleware
from store.models.model_product import Product


class Cart(View):
    @method_decorator(auth_middleware) 
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request, 'cart.html', {'products':products})
            