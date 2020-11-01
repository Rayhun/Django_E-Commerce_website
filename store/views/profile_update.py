from django.shortcuts import render, redirect
from django.views import View
from store.models.model_customer import Customer

from .forms import CustomerForm

class ProfileUpdate(View):

    def get(self, request, *args, **kwargs):
        form = CustomerForm(instance=Customer.objects.filter(
            pk=request.session.get('customer_id')).first())
        return render(request, 'profile_update.html',{'form':form})


    def post(self, request, *args, **kwargs):
        customer = request.session.get('customer_id')
        obj = Customer.objects.filter(pk=customer).first()
        form = CustomerForm(self.request.POST, self.request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'profile_update.html',{'form':form})
            
            