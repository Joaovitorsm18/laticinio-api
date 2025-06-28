from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.SaleCreateList.as_view(), name='sale-create-list'),
    path('sales/<int:pk>/', views.SaleRetrieveUpdateDestroyView.as_view(), name='sale-detail'), 
    path('sales/report', views.SaleReportView.as_view(), name='sales-report'),
]