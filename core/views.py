from django.shortcuts import render

# Create your views here.
from .models import Habit, Result
from .forms import HabitForm

def habit_list(request):
    return render(request, 'core/habit_list.html')

def habit_add(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit-detail', pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, 'core/habit_add.html', {'form':form})