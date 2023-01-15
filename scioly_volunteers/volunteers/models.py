from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Tournament(models.Model):
    duosmium_id = models.CharField(max_length=100, blank=True, unique=True)
    name = models.CharField(max_length=100)
    date = models.DateField()

    @property
    def season(self):
        return self.date.year if self.date.month < 7 else self.date.year + 1


class State(models.Model):
    name = models.CharField(max_length=25, unique=True)
    abbreviation = models.CharField(max_length=4, unique=True)
