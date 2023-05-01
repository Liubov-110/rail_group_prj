from django.urls import path
from . import views

app_name = 'routes'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_routes, name='search_routes'),
    path('route/<int:pk>/', views.RouteDetailView.as_view(), name='route_detail'),
    path('route/create/', views.RouteCreateView.as_view(), name='route_create'),
    path('route/update/<int:pk>/', views.RouteUpdateView.as_view(), name='route_update'),
    path('route/delete/<int:pk>/', views.RouteDeleteView.as_view(), name='route_delete'),
    path('route/save/<int:pk>/', views.save_route, name='save_route'),
]
