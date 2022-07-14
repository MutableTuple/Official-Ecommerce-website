from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.Home, name="home" ),
    path('product/<str:pk>', views.Products_View, name = 'products'),
    path('register/', views.UserRegistraion, name = 'register'),
    path('login/', views.LoginUser, name = 'login'),
    

    
]
