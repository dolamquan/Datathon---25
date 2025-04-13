from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('result/',views.result, name='result'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
]