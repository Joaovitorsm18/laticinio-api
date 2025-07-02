from rest_framework import serializers
from customers.models import Customer
from sales.serializers import SaleSerializer

class CustomerSerilizer(serializers.ModelSerializer):
    sales = SaleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'name', 'nickname', 'customer_type', 'sales']