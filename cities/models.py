from django.db import models

class City(models.Model):
    class Meta:
        verbose_name = 'Населений пункт'
        verbose_name_plural = 'Населені пункти'
        ordering = ["name"]
    
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name = 'Населений пункт')

    def __str__(self):
        return self.name
