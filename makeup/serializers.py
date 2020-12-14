from rest_framework import serializers
from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(
        source='product.name', read_only=True)


class Meta:
    model = Product
    fields = ('id', 'title', 'product_name', 'color', 'photo_url')


class Meta:
    model = Comment
    fields = ('id', 'user', 'body', 'post')
