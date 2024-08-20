from .models import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id', 'name', 'category', 'price', 'quantity_in_stock']