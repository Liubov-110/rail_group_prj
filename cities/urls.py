from django.urls import path
from . import views


urlpatterns = [
    path('', views.city_list, name='city_list'),
    path('add/', views.city_create, name='city_create'),
    path('<int:pk>/', views.city_detail, name='city_detail'),
    path('<int:pk>/edit/', views.city_update, name='city_update'),
    path('<int:pk>/delete/', views.city_delete, name='city_delete'),
]