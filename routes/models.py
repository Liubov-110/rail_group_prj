from django.db import models
from cities.models import City

class Route(models.Model):
    start_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_start_city_set', verbose_name='Початкове місто')
    end_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_end_city_set', verbose_name='Кінцеве місто')
    travel_time = models.IntegerField(verbose_name='Час у дорозі')
    name = models.CharField(max_length=50, unique=True, verbose_name='Назва маршруту')
    cities = models.ManyToManyField(City, blank=True, verbose_name='Проміжні міста')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'
        ordering = ['travel_time']
