from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('student/<int:student_id>/', views.student_profile, name='student_profile'),
]
