from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    goal = models.PositiveIntegerField()
    # we may need to change DateField
    date = models.DateField()
    # goal_met = models.BooleanField(default=False)

    def __str__(self):
        return f" Habit name: {self.name} goal: {self.goal} date: {self.date}"

class Result(models.Model):
    progress = models.PositiveIntegerField(null=True, blank=True)
    habit = models.ForeignKey("Habit", on_delete=models.CASCADE, related_name="results")
    date = models.DateField(default=datetime.date.today)



    def __str__(self):
        return f"Result progress: {self.progress} habit: {self.habit} date: {self.date}"

    class Meta:
        unique_together = ('progress', 'habit')

# class Observer: