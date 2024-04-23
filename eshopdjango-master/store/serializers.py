from rest_framework import serializers
from .models.customer import Customer
from .models.category import Category
from .models.product import Product
from .models.orders import Order
from .models.orders import Order



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




