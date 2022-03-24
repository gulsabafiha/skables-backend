from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
   path('users/',getUser),
   path('product/<int:pk>/',product_detail),
   path('user/profile/',getUserProfile,name='user-profile'),
   path('user/register/',registerUser,name='register'),
   path('profile/update/',updateUserProfile,name='profile-update'),
 
]
