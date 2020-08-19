from django.urls import path
from . import views

app_name = 'Manage'
urlpatterns = [
    path('manage/', views.index, name='Index'),
    path('manage/#rfid', views.index, name='Index rfid'),
    path('manage/#users', views.index, name='Index users'),
    path('manage/#pin', views.index, name='Index pin'),
    path('manage/#sysinfo', views.index, name='Index System info'),
    path('manage/rfid/new/', views.NewTag.as_view(), name='New Rfid'),
    path('manage/user/new/', views.NewUser.as_view(), name='New User'),
    path('manage/rfid/<pk>/edit/', views.EditTag.as_view(), name='Edit Rfid'),
]
