from rest_framework import serializers
from sales.models import Sale, SaleItem
import os
import json
from django.utils.text import slugify


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'unit', 'quantity', 'unit_price', 'total_price']
        read_only_fields = ['total_price']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError('Quantidade deve ser maior que zero.')
        if round(value, 3) != value:
            raise serializers.ValidationError('Máximo de 3 casas decimais permitidas.')
        return value

    def validate_unit_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Preço unitário não pode ser negativo.')
        return value

class SaleSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    items = SaleItemSerializer(many=True, required=False)

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'date', 'status', 'receipt_photo', 'items', 'total']

    def validate(self, attrs):
        raw_items = self.initial_data.get('items')

        if not raw_items:
            raise serializers.ValidationError({'items': 'A venda deve conter ao menos um item.'})

        # Converte string JSON para lista de dicionários, se necessário
        if isinstance(raw_items, str):
            try:
                items_list = json.loads(raw_items)
            except json.JSONDecodeError:
                raise serializers.ValidationError({'items': 'Formato JSON inválido.'})
        else:
            items_list = raw_items

        # Validação final
        if not isinstance(items_list, list) or not all(isinstance(i, dict) for i in items_list):
            raise serializers.ValidationError({'items': 'Formato inválido para lista de itens.'})

        item_serializer = SaleItemSerializer(data=items_list, many=True)
        item_serializer.is_valid(raise_exception=True)

        self._validated_items = item_serializer.validated_data
        return attrs


    def create(self, validated_data):
        validated_data.pop('items', None)  # remove para evitar erro
        sale = Sale.objects.create(**validated_data)

        for item_data in self._validated_items:
            SaleItem.objects.create(sale=sale, **item_data)


        return sale

    def update(self, instance, validated_data):
        # Remove os itens validados de validated_data para evitar conflito
        validated_data.pop('items', None)

        # Atualiza os campos simples da venda
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Atualiza os itens se forem enviados
        if hasattr(self, '_validated_items'):
            instance.items.all().delete()
            for item_data in self._validated_items:
                SaleItem.objects.create(sale=instance, **item_data)

        return instance
