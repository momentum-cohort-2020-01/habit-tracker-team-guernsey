from django import forms

from .models import Habit, Result

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'goal', 'date')

class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ('progress',)