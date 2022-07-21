from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductDelete(generics.DestroyAPIView):
#     queryset = Product.delete
#     serializer_class = ProductSerializer

