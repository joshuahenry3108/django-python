from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
from django.http import JsonResponse
from datetime import datetime

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def cached_data_view(request):
    cache_key = "sample:data"
    data = cache.get(cache_key)

    if data:
        print("📦 Cache hit")
        return JsonResponse(data)

    # Simulate fresh data
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Fresh data from backend"
    }

    cache.set(cache_key, data, timeout=60)  # 60 seconds
    print("💾 Cache miss — new data stored")
    return JsonResponse(data)
