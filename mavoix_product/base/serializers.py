from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['prod_id', 'serial_no', 'catagory', 'family', 'image', 'short_desc', \
                  'long_desc', 'specification', 'stock', 'batch_no', 'certification']
