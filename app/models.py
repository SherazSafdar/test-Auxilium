from django.db import models
import uuid
from django.contrib.auth.models import User

class Item(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=75)
    category = models.CharField(max_length=75)
    price = models.FloatField()
    quantity_in_stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} ({self.category})"


class PurchaseOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)