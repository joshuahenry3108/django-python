from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse



def health_check(request):
    return JsonResponse({"status": "working"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),   # ✅ This line is important
    path('health', health_check),
]