from django.db import models

# Create your models here.

class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Quilo'),
        ('un', 'Unidade'),
        ('lt', 'Litro'),
    ]

    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
