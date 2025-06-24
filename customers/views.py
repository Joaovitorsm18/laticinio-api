from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerilizer


class CustomerCreateListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer


