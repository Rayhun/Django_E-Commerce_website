from django.urls import path
from .views.home import Index
from .views.login import Login
from .views.signup import Signup
from .views.login import logout
from .views.cart import Cart
from .views.chackout import Chackout
from .views.order import OrderView
from django.utils.decorators import method_decorator

from store.middlewares.auth import auth_middleware
urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', auth_middleware(Cart.as_view()), name='cart'),
    path('chackout/', auth_middleware(Chackout.as_view()), name='chackout'),
    path('orders/',auth_middleware(OrderView.as_view()), name='orders'),
]
