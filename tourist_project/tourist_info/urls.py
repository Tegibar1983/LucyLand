from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), #127.0.0.1:8000/home/
    path('create_region/', views.create_region, name='create_region'), #127.0.0.1:8000/create_region
    path('read_more/<int:pk>', views.read_more, name='read_more'), #127.0.0.1:8000/read_more
    path('update_region/<int:pk>', views.update_region, name='update_region'), #127.0.0.1:8000/update_region/1
    path('delete_region/<int:pk>', views.delete_region, name='delete_region'), #127.0.0.1:8000/delete_region/1
    path('register_user/', views.register_user, name='register_user'), #127.0.0.1:8000/register_user
]


