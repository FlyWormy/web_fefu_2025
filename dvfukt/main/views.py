from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FeedbackForm, RegistrationForm


# Существующие представления
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def student_profile(request, student_id):
    if student_id > 100:
        return render(request, 'main/student_profile.html', {
            'error': f'Студент с ID {student_id} не найден'
        }, status=404)
    return render(request, 'main/student_profile.html', {
        'student_id': student_id
    })


# Новые представления для форм
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Здесь можно сохранить в базу или отправить email
            messages.success(request, 'Спасибо за ваш отзыв! Мы свяжемся с вами в ближайшее время.')
            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'main/feedback.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Создание пользователя
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(request, f'Пользователь {username} успешно зарегистрирован!')
            return redirect('register')
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})