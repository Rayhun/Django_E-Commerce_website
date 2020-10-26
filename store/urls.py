from django.urls import path
from .views.home import Index
from .views.login import Login
from .views.signup import Signup
from .views.login import logout
from .views.cart import Cart
from .views.chackout import Chackout

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('chackout/', Chackout.as_view(), name='chackout'),
]
