from django.urls import path
from . import views

app_name = 'Review'
urlpatterns = [
    path('review/', views.review_index, name='Index'),
    path('review/#videos', views.review_index, name='Index videos'),
    path('review/#log', views.review_index, name='Index log'),
    path('review/video/download/<str:file>/', views.download, name='download video'),
    path('review/log/download/', views.download_log, name='download log'),
    path('review/video/delete/<str:file>/', views.delete, name='delete video'),
    path('review/video/downloadall/', views.download_all_videos, name='download all videos'),
    path('review/video/deleteall/', views.delete_all_videos, name='delete all videos'),
    path('review/ajax/video_info/', views.video_info, name='Get video info'),


]