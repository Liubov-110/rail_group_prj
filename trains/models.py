# from django.db import models
# #from django.core.validators import MaxValueValidator 
# #from django.core.validators import RegexValidator



# class Train(models.Model):
#     #train_number = models.IntegerField(max_length=10) https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield
#     #train_number = models.IntegerField(validators=[MaxValueValidator(9999999999)]) 
#     # or train_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')]
#     begin_of_route = models.CharField(max_length=50)
#     begin_of_route = models.CharField(max_length=50)
#     travel_time = models.DurationField()

#     def __str__(self):
#         return self.train_number
from django.db import models
from cities.models import City

class Train(models.Model):
    name = models.CharField(max_length=100)
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city')
    travel_time = models.IntegerField()

    def __str__(self):
        return f'Train {self.name} from {self.from_city} to {self.to_city}'