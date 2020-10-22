from django.urls import path
from .views.home import Index
from .views.login import Login
from .views.signup import Signup

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
]
