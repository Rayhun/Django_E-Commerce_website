from django.shortcuts import render, redirect
from django.views import View

from store.models.model_product import Product
from store.models.model_category import Category
from store.models.model_customer import Customer

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1 # increment  
                else:
                    cart[product] = quantity + 1 # decrement
            else:
                cart[product] = 1 # New Add
        else:
            cart = {}
            cart[product] = 1 
        request.session['cart'] = cart
        return redirect("home")

    def get(self, request):
        products = None
        categorys = Category.objects.all()
        categoryID = request.GET.get('category')

        
        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        contex = {
            'products':products,
            'categorys':categorys,
        }
        return render(request, 'index.html', contex)