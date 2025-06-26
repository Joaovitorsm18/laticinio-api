from django.contrib import admin
from sales.models import Sale, SaleItem


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer','date', 'status', 'receipt_photo', 'total')

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'product', 'unit', 'quantity', 'unit_price', 'total_price')