from django.db import models

class Train(models.Model):
    train_number = models.IntegerField(max_length=10)
    begin_of_route = models.CharField(max_length=50)
    begin_of_route = models.CharField(max_length=50)
    travel_time = models.DurationField()

    def __str__(self):
        return self.train_number
