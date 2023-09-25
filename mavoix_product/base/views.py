from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class ProductView(ListAPIView):
    
