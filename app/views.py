from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status


class ItemAPIView(APIView):
    def get(self, request, item_id=None):
        if item_id:
            try:
                item = Item.objects.get(id=item_id)
                serializer = ItemSerializer(item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Item.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            category = request.GET.get('category')
            sort_by = request.GET.get('sort_by')
            items = Item.objects.all()

            if category:
                items = items.filter(category=category)

            if sort_by in ['price', 'quantity_in_stock']:
                items = items.order_by(sort_by)

            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, item_id):
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoestNotExist:
            return Response({"error": "Item Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
