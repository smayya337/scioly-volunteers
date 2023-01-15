from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Tournament(models.Model):
    duosmium_id = models.CharField(max_length=100, blank=True, unique=True)
    name = models.CharField(max_length=100)
    date = models.DateField()


class State(models.Model):
    name = models.CharField(max_length=25, unique=True)
    abbreviation = models.CharField(max_length=4, unique=True)


class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
