from django.urls import path
from . import views

app_name = 'trains'

urlpatterns = [
    # шлях для перегляду списку поїздів
    path('', views.train_list, name='train_list'),
    
    # шлях для додавання нового поїзда
    path('add/', views.train_add, name='train_add'),
    
    # шлях для редагування поїзда з певним ідентифікатором
    path('<int:pk>/edit/', views.train_edit, name='train_edit'),
    
    # шлях для видалення поїзда з певним ідентифікатором
    path('<int:pk>/delete/', views.train_delete, name='train_delete'),
]
