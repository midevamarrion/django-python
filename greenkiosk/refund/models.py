from django.db import models

# Create your models here.
class Refund(models.Model):
    class Meta:
        verbose_name_plural = "refund"
    item_ordered = models.CharField(max_length=32)
    requested_time = models.DateTimeField()
    reason = models.CharField(max_length=32)
    approval = models.BooleanField()

