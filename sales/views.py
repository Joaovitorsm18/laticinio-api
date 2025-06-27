from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from sales.models import Sale, SaleItem
from sales.serializers import SaleSerializer, SaleItemSerializer
from sales.filters import SaleFilter

class SaleCreateList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all().order_by('date')
    serializer_class = SaleSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]

class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleItemCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

class SaleItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer


class SaleReportView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all().prefetch_related('items', 'customer').order_by('date')
    serializer_class = SaleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleFilter
    # opcional: permitir ordenação
    ordering_fields = ['date', 'customer__name', 'status']
    ordering = ['-date']