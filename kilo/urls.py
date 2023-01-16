from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jpg/<int:file_id>/', views.make_jpg, name='jpg'),
    path('png/<int:file_id>/', views.make_png, name='png'),
]
