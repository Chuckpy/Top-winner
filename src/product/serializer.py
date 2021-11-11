from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'name', 'slug', 'description', 'reference_code', 
            'internal_code','price', 'is_available', 
        )
