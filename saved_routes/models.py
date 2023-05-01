from django.db import models
from django.contrib.auth.models import User
from routes.models import Route

class SavedRoute(models.Model):
    class Meta:
        verbose_name = 'Збережений маршрут'
        verbose_name_plural = 'Збережені маршрути'
        ordering = ['route']

    name = models.CharField(max_length=100, verbose_name='Назва')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Маршрут')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    date_saved = models.DateTimeField(auto_now_add=True, verbose_name='Дата збереження')

    def __str__(self):
        return self.name
 