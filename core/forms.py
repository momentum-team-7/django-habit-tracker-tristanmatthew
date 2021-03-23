from django import forms
from .models import User, Habit, HabitTracker, Profile

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'title', 
            'description',
            'goal', 
            'goal_type',
        ]

class TrackerForm(forms.ModelForm):
    class Meta:
        model = HabitTracker
        fields = [
            'habit',
            'amount',
            'completed',
            'date',
        ]