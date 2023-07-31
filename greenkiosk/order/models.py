from django.db import models
from customer.models import Customer
from delivery.models import Delivery
from cart.models import Cart

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    deliver = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    order_status  = models.CharField(max_length=10)
    items = models.CharField(max_length=10)
    customer_information  = models.CharField(max_length=15)
    payment_details = models.PositiveIntegerField()
