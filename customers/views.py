from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from customers.models import Customer
from customers.serializers import CustomerSerilizer


class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer


