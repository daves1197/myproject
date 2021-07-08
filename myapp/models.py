from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
import datetime


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64, blank=True)

class Seminar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    seminar_titel = models.CharField(max_length=100, default="")
    seminar_description = models.CharField(max_length=250, default="")
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default='08:00')
    end_time = models.TimeField(default='20:00')
    is_leader = models.BooleanField(default=False)
    url_image = models.URLField(default="google.com", null=True, blank=True)
    category = models.CharField(max_length=64, blank=True, default="")
    seminar_rating = models.IntegerField(default=0)
    counter = models.IntegerField(default=1)
    is_ended = models.BooleanField(default=False)

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #deleting references Objects this should be deleted too
    comment = models.TextField(max_length=100)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} has written"

class Partis(models.Model):
    part = models.ForeignKey(User,  blank=True, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar,  blank=True, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=100)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
