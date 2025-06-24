from rest_framework import serializers
from customers.models import Customer

class CustomerSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'