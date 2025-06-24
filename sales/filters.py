from django_filters import rest_framework as filters
from sales.models import Sale
from customers.models import Customer
from products.models import Product

class SaleFilter(filters.FilterSet):
    # filtrar data entre duas datas
    date = filters.DateFromToRangeFilter()
    # filtrar por cliente (pelo ID)
    customer = filters.ModelChoiceFilter(
        field_name='customer',
        queryset=Customer.objects.all()
    )
    # filtrar por status
    status = filters.ChoiceFilter(choices=Sale.STATUS_CHOICE)
    # filtrar por produto presente nos items
    product = filters.ModelChoiceFilter(
        field_name='items__product',
        queryset=Product.objects.all(),
        label='Produto'
    )

    class Meta:
        model = Sale
        # o name do FilterSet aqui permite passar parametros:
        # ?date_after=2025-01-01&date_before=2025-01-31&customer=2&status=paid&product=5
        fields = ['date', 'customer', 'status', 'product']
