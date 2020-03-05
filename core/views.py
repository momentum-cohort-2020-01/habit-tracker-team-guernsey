from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Result
from .forms import HabitForm, ResultForm

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

def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit-list')
    
def habit_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance = habit)
        if form.is_valid():
            habit.save()
            return redirect('habit-details', habit.pk)
    else:
        form = HabitForm(instance = habit)
        return render(request, 'core/habit_edit.html', {'form':form})    

def show_progress(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'core/habit_details.html', {'habit':habit, 'pk':pk})


def progress_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = ResultForm(request.POST, instance = habit)
        if form.is_valid():
            progress.save()
            return redirect('habit-details', habit.pk)
    else:
        form = ResultForm(instance = habit)
        return render(request, 'core/habit_details.html', {'form':form})
