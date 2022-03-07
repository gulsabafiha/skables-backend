from django.urls import path
from .views import *



urlpatterns = [
   path('',UserViewSet),
   path('product/<int:pk>/',product_detail),
 
]
