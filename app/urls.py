from django.urls import path
from .views import ItemAPIView

urlpatterns = [
    path('items/', ItemAPIView.as_view(), name='item_list'),
    path('items/<uuid:item_id>/', ItemAPIView.as_view(), name ='item_detail')
]
