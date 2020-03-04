from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Result
from .forms import HabitForm

@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_list.html', {'habits': habits})

def habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'core/habit_details.html', {'habit':habit, 'pk':pk})

def habit_add(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit-details', pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, 'core/habit_add.html', {'form':form})
