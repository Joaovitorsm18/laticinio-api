from rest_framework import serializers
from sales.models import Sale, SaleItem

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = '__all__'
        read_only_fields = ['total_price']

class SaleSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    items = SaleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'

