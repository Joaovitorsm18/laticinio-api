from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.SupllierCreateListView.as_view(), name='supplier-create-list'),
    path('suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
]

