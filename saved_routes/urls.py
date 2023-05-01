from django.urls import path
from . import views

app_name = 'saved_routes'

urlpatterns = [
    path('', views.savedroute_list, name='saved_route_list'),
    path('<int:pk>/', views.savedroute_detail, name='saved_route_detail'),
    path('new/', views.savedroute_new, name='saved_route_create'),
]
