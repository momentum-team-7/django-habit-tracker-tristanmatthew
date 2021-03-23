from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import User, Habit, HabitTracker, Profile
from .forms import HabitForm, TrackerForm

# Create your views here.

def index(request):
    return render(request, 'index.html/', {})

def userindex(request):
    habits = Habit.objects.all().order_by('-id')
    return render(request, 'userindex.html/', {'habits': habits })

def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.author = request.user
            form.save()
            return HttpResponseRedirect('/userindex/')

    else:
        form = HabitForm()

    return render(request, 'add_habit.html', {'form': form })

def habit_detail(request):
    profile = get_object_or_404(Profile, user=request.user)
    habits = Habit.objects.filter(user=profile.user)
    return render(request, 'habit_detail.html',{'profile': profile, 'habits': habit})


