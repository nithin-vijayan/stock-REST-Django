from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length = 10)
    open_value  = models.FloatField()
    close_value = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker
