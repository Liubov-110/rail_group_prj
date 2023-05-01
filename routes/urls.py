from django.urls import path
from . import views

urlpatterns = [
    # шлях для пошуку маршруту
    path('routes/search/', views.route_search, name='route_search'),

    # шлях для детальної інформації про маршрут
    path('routes/<int:pk>/', views.route_detail, name='route_detail'),

    # шлях для відображення результатів пошуку маршруту
    path('routes/results/', views.route_results, name='route_results'),
]
