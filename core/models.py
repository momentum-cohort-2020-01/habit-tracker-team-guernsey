from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=50)
    goal = models.TextField()
    date = models.DateField()
    # we may need to change DateField
    result = models.ForeignKey("Result", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f" Habit name: {self.name} goal: {self.goal} date: {self.date}"

class Result(models.Model):
    recording = models.TextField()
    goal_met = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

# class Observer: