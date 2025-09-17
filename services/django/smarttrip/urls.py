from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to SmartTrip Django API"})

urlpatterns = [path("", home)]
