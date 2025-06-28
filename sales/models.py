import os
from datetime import datetime
from django.utils.text import slugify
from django.db import models
from django.db.models import Sum
from customers.models import Customer
from products.models import Product
from django.utils import timezone


def custom_receipt_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.now().strftime("%Y-%m-%d")
    filename = f"recibo_venda_novo_{now}.{ext}"
    return os.path.join("sales_receipts", slugify(filename))


class Sale(models.Model):
    STATUS_CHOICE = [
        ('paid',    'Pago'),
        ('pending', 'Pendente'),
        ('negotiated', 'Negociado'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='sales')
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='pending')
    receipt_photo = models.ImageField(upload_to='sales_receipts/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    @property
    def total(self):
        return self.items.aggregate(total=Sum('total_price'))['total'] or 0
    
    def __str__(self):
        return f"Venda #{self.id} — {self.customer.name} ({self.get_status_display()})"
  
    
class SaleItem(models.Model):
    sale        = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product     = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit        = models.CharField(max_length=10, choices=Product.UNIT_CHOICES)
    quantity    = models.DecimalField(max_digits=10, decimal_places=3)
    unit_price  = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, editable=False)


    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} {self.get_unit_display()} de {self.product.name}"