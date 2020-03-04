from django.shortcuts import render

# Create your views here.
from .models import Habit, Result

def habit_list(request):
    return render(request, 'core/habit_list.html')