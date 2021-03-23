from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class Habit(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400, blank=True, null=True)
    goal = models.IntegerField(default=0)
    goal_type = models.CharField(max_length=100)
    tracker = models.ForeignKey("HabitTracker", on_delete=models.CASCADE, related_name="tracker", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.habit

class HabitTracker(models.Model):
    
    class Answer(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')

        __empty__ = _('(Unknown)')

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="tracking")
    amount = models.IntegerField(default=0)
    completed = models.IntegerField(choices=Answer.choices)
    date = models.DateField()

    def __str__(self):
        return f'{self.amount}'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f'{self.user}'