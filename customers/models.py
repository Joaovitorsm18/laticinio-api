from django.db import models

# Create your models here.

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ("fair", "Feira"),
        ("store", "Comércio"),
    ]
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPES)

    def __str__(self):
        return self.name 