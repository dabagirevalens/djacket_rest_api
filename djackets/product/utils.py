from itertools import product
from pydoc import describe
from django.db.models import Q

from .models import Product


def searchProduct(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    products = Product.objects.filter(
        Q(name__icontains=search_query) | Q(description__icontains=search_query))
    
    return products

