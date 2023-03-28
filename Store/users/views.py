from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, UserRegForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегистрировались!')
            return HttpResponseRedirect('/')
    else:
        form = UserRegForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return 1
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Я каменщик', 'form': form}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

