from django.contrib.auth.models import AbstractUser
from django.db import models
from scioly_volunteers.volunteers.models import Event, State, Tournament


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)

    events = models.ManyToManyField(Event, blank=True)
    tournaments = models.ManyToManyField(Tournament, blank=True)
    states = models.ManyToManyField(State, blank=True)
    bio = models.CharField(max_length=2000, blank=True)
    years_of_experience = models.IntegerField(blank=True)
    publish_data = models.BooleanField(default=False)

    @property
    def events_string(self):
        return ", ".join([e.name for e in self.events.all()])
