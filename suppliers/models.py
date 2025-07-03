from django.db import models

SUPPLIER_CHOICES = (
    ("wholesaler", "Atacado"),
    ("producer", "Produtor"),
    ("other", "Outros"),
)


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    supplier_type = models.CharField(max_length=30, choices=SUPPLIER_CHOICES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name