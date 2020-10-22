from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from store.models.model_customer import Customer


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        customer = Customer.get_customer_by_username(username)
        error_message = None
        if customer:
            flug = check_password(password, customer.password)
            if flug:
                request.session['customer_id'] = customer.id
                request.session['username'] = customer.username
                return redirect('home')
            else:
                error_message = "Email or Password Not Match"
        else:
            error_message = "Email or Password Not Match"
        return render (request, 'login.html', {'error': error_message})
        