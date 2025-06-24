from django.db import models
from django.db.models import Sum
from django.forms import ValidationError
from customers.models import Customer
from products.models import Product
from django.utils import timezone

# Create your models here.

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

    @property
    def total(self):
        return self.items.aggregate(total=Sum('total_price'))['total'] or 0

    def __str__(self):
        return f"Venda #{self.id} — {self.customer.name} ({self.get_status_display()})"
    
class SaleItem(models.Model):
    sale        = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product     = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit        = models.CharField(max_length=10, choices=Product.UNIT_CHOICES)
    quantity    = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price  = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)


    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantidade deve ser maior que zero.")
        if self.unit_price < 0:
            raise ValidationError("Preço unitário não pode ser negativo.")

    def save(self, *args, **kwargs):
        # calcula total antes de salvar
        self.full_clean()
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} {self.get_unit_display()} de {self.product.name}"