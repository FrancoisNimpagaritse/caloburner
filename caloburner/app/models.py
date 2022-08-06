from django.db import models


# Create your models here.
class Metric(models.Model):
    sport_day = models.DateTimeField(auto_now_add=True)
    distance_done = models.FloatField()

    def __str__(self):
        return str(self.sport_day) + ' -> ' + str(self.sport_hour)
