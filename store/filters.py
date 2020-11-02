import django_filters
from django_filters import CharFilter

from store.models.model_order import Order
from store.models.model_product import Product
class OrderFlteri(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['price','product','status']

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
        }