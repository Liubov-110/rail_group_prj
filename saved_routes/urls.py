from django.urls import path
from . import views

app_name = 'saved_routes'

urlpatterns = [
    path('', views.SavedRouteListView.as_view(), name='saved_route_list'),
    path('<int:pk>/', views.SavedRouteDetailView.as_view(), name='saved_route_detail'),
    path('new/', views.SavedRouteCreateView.as_view(), name='saved_route_create'),
]
