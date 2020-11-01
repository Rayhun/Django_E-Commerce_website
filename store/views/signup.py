from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View

from store.models.model_customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        username = postData.get('username')
        email = postData.get('email')
        mobile = postData.get('mobile')
        gender = postData.get('gender')
        password = postData.get('password')
        
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'username' : username,
            'email' : email,
            'mobile' : mobile,
            'gender' :gender,
        }

        customer = Customer(first_name=first_name, 
                                last_name=last_name, 
                                username=username, 
                                email=email,  
                                mobile=mobile,  
                                gender=gender,
                                password=password
                                )

        error_message = self.validatCustomer(customer)

        if not error_message:

            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        contex = {
            'error':error_message,
            'values':value
        }
        return render(request, 'signup.html',contex)
    def validatCustomer(self, customer):
        error_message = None
        if not customer.first_name:
                error_message = "First Name is Requiered!"
        elif len(customer.first_name) < 4 :
            error_message = 'First name is too short'
        elif not customer.last_name:
            error_message = "Last Name is Requiered!"
        elif len(customer.last_name) < 4:
            error_message = 'Last Name is too short' 
        elif not customer.username:
            error_message = "Username is Requiered!"
        elif len(customer.username) < 4:
            error_message = 'Username is too short'
        elif Customer.objects.filter(username=customer.username):
            error_message = 'Username Already Registered!'
        elif not customer.email:
            error_message = "Email is Requiered!"
        elif Customer.objects.filter(email=customer.email):
            error_message = 'Email Already Registered!'
        elif len(customer.email) < 4:
            error_message = 'email is too short'
        elif len(customer.mobile) < 5:
            error_message = "Chack Your Number"
        elif not customer.gender:
            error_message = "gender is requiered"
        elif not customer.password:
            error_message = "password is required"
        elif len(customer.password) < 6:
            error_message = "Password minimum six digit required"
        return error_message
