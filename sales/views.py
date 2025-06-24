from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from sales.models import Sale, SaleItem
from sales.serializers import SaleSerializer, SaleItemSerializer
from sales.filters import SaleFilter

class SaleCreateList(generics.ListCreateAPIView):
    queryset = Sale.objects.all().order_by('date')
    serializer_class = SaleSerializer

class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleItemCreateListView(generics.ListCreateAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

class SaleItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer


class SaleReportView(generics.ListAPIView):
    """
    Lista vendas com filtros de data, cliente, status e produto.
    """
    queryset = Sale.objects.all().prefetch_related('items', 'customer').order_by('date')
    serializer_class = SaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleFilter
    # opcional: permitir ordenação
    ordering_fields = ['date', 'customer__name', 'status']
    ordering = ['-date']