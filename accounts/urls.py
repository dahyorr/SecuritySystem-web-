from django.urls import path
from . import views

app_name = 'Accounts'
urlpatterns = [
    path('login/', views.LogIn.as_view(), name='Login'),
    path('accounts/login/', views.LogIn.as_view(), name='Login'),
    path("logout/", views.LogOut.as_view(), name="Logout"),
    path('', views.Home.as_view(), name='Home'),

]