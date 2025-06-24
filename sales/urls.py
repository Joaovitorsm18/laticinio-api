from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.SaleCreateList.as_view(), name='sale-create-list'),
    path('sales/<int:pk>/', views.SaleRetrieveUpdateDestroyView.as_view(), name='sale-detail'),    
    path('sale-items/', views.SaleItemCreateListView.as_view(), name='saleitem-create-list'),
    path('sale-items/<int:pk>/', views.SaleItemRetrieveUpdateDestroyView.as_view(), name='saleitem-detail'),
    path('sales/report', views.SaleReportView.as_view(), name='sales-report'),
]