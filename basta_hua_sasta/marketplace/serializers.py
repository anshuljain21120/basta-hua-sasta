from rest_framework import serializers
from basta_hua_sasta.marketplace.models import Product, CartItem, Order


class ProductSerializer(serializers.ModelSerializer):
    seller_name = serializers.SerializerMethodField(method_name='get_seller_name')

    class Meta:
        model = Product
        fields = '__all__'
        extra_fields = ['seller_name']

    @staticmethod
    def get_seller_name(product: Product):
        return product.owner.get_full_name()

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'
