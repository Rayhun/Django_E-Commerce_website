from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View

from store.models.model_customer import Customer


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
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
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                return redirect('home')

            else:
                error_message = "Email or Password Not Match"
        else:
            error_message = "Email or Password Not Match"
        return render (request, 'login.html', {'error': error_message})
        
def logout(request):
    request.session.clear()
    return redirect('login')