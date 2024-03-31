from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Используем email в качестве username
            user.save()
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']  # Изменяем на email
            password = form.cleaned_data['Пароль']
            # Используем email вместо username
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('posts')

        messages.error(request, f'Неверный email или пароль')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    # messages.success(request, f'You have been logged out.')
    return redirect('home')


def home(request):
    return render(request, 'home.html')
