from django.db import models
from django.contrib.auth.models import User
from routes.models import Route

class SavedRoute(models.Model):
    name = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
 