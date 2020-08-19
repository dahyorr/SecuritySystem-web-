from django.urls import path
from . import views
app_name = 'Gui'
urlpatterns = [
    path('gui/', views.gui_changer, name='gui main'),
    path('gui/page/', views.check_page, name='check page'),
    path('gui/html/', views.get_content, name='check page')
]
