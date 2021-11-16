from django.db import models
from datetime import datetime

class data(models.Model):
    date = models.DateField(verbose_name="Date", default=datetime.now())
    views = models.IntegerField(verbose_name="Views", unique=False)
    clicks = models.IntegerField(verbose_name="Clicks", unique=False)
    cost = models.FloatField(verbose_name="Cost", unique=False)

    def __str__(self):
        return str(self.date)
    
