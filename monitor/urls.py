from django.urls import path
from . import views

app_name = 'Monitor'
urlpatterns = [
    path('monitor/', views.Home.as_view(), name='Home'),

]