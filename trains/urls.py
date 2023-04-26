from django.urls import path
from . import views

app_name = 'trains'

urlpatterns = [
    # шлях для перегляду списку поїздів
    path('', views.TrainListView.as_view(), name='train_list'),
    
    # шлях для додавання нового поїзда
    path('add/', views.TrainCreateView.as_view(), name='train_add'),
    
    # шлях для редагування поїзда з певним ідентифікатором
    path('<int:pk>/edit/', views.TrainUpdateView.as_view(), name='train_edit'),
    
    # шлях для видалення поїзда з певним ідентифікатором
    path('<int:pk>/delete/', views.TrainDeleteView.as_view(), name='train_delete'),
]
