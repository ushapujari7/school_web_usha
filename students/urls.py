from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
]
