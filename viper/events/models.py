from django.db import models
from django.db.models.fields import CharField

from django.contrib.auth.models import User

class EventModel(models.Model):

    MODE = (
        ("Online", "Online"),
        ("Offline", "Offline")
    )

    title = models.CharField(max_length=255)
    descript = models.CharField(max_length=255)
    platform_name = models.CharField(max_length=255)
    platform_mode =  models.CharField(choices=MODE, max_length=10)
    starting_date = models.DateField()
    ending_date = models.DateField()
    photo = models.ImageField(upload_to='event_photo/', null = True, blank=True)
    thumbnail = models.ImageField(upload_to='event_thumbnail/', null=True, blank=True)

    coordinator =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title