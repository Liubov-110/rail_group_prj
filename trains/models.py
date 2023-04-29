from django.db import models
from cities.models import City


class Train(models.Model):
    class Meta:
        verbose_name = 'Поїзд'
        verbose_name_plural = 'Поїзда'
        ordering = ["-name"]
    
    name = models.CharField(max_length=100, unique=True, blank=False, verbose_name = 'Номер поїзда')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city', verbose_name = 'Відправлення')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city', verbose_name = 'Прибуття')
    travel_time = models.IntegerField(verbose_name = 'Час в дорозі')

    def __str__(self):
        return f'Поїзд №: {self.name} - відправлення:=> {self.from_city} -=- прибуття: =>{self.to_city}'