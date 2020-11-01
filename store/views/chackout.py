from django.shortcuts import render, redirect
from django.views import View
from store.models.model_product import Product
from store.models.model_order import Order
from store.models.model_customer import Customer

class Chackout(View):
    def post(self, request):
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        
        products = Product.get_product_by_id(list(cart.keys()))
        for product in products:
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price= product.price,
                address = address,
                mobile=mobile,
                quantity=cart.get(str(product.id))
            )
            order.save()
        
        request.session['cart'] = {}
        return redirect('cart')