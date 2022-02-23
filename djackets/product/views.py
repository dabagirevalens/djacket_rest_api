from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from .utils import searchProduct


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductDeatails(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetails(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProductSearch(APIView):
    def get(self, request, format=None):
        products = searchProduct(request)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
