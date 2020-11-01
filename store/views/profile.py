from django.shortcuts import render, redirect
from django.views import View
from store.models.model_product import Product
from store.models.model_order import Order
from store.models.model_customer import Customer

class Profile(View):
    def get(self, request, *args, **kwargs):
        customer_id = request.session.get('customer_id')
        username = request.session.get('username')
        customer = Customer.get_customer_by_username(username)
        if customer:
           first_name = request.session['first_name'] = customer.first_name
           last_name = request.session['last_name'] = customer.last_name
           email = request.session['email'] = customer.email
           mobile = request.session['mobile'] = customer.mobile
           gender = request.session['gender'] = customer.gender
           bio = request.session['bio'] = customer.bio
           birth_day = request.session['birth_day'] = customer.birth_day
        context = {
            'customer_id':customer_id,
            'customer': customer,
            'first_name': first_name,
            'last_name':last_name,
            'username': username,
            'email': email,
            'mobile':mobile,
            'gender': gender,
            'bio': bio,
            'birth_day': birth_day,
        }
        
        return render(request, 'profile.html',context)
# from django.shortcuts import render, redirect
# from django.views import View
# from store.models.model_product import Product
# from store.models.model_order import Order
# from store.models.model_customer import Customer

# from .forms import CustomerForm
# class Profile(View):
#     def get(self, request, *args, **kwargs):
#         ids=request.session.get('customer_id')
#         form = CustomerForm(instance=Customer.objects.filter(pk=request.session.get('customer_id')).first())
#         context = {
#             'ids':ids,
#             'form':form
#         }
#         return render(request, 'profile.html',context)