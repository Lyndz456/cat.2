from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the e-commerce system.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Order(models.Model):
    """
    Represents an order placed by a customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # One-to-Many relationship
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-order_date']  # Orders listed with the most recent first