from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def student_profile(request, student_id):
    if student_id > 100:
        return render(request, 'main/student_profile.html', {
            'error': f'Студент с ID {student_id} не найден. Попробуйте ID от 1 до 100.'
        }, status=404)

    return render(request, 'main/student_profile.html', {
        'student_id': student_id
    })