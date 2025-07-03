from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer

class SupllierCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer