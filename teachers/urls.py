from django.urls import path
from .views import teacher_list, add_teacher, edit_teacher, delete_teacher, teacher_detail

urlpatterns = [
    path('', teacher_list, name='teacher_list'),
    path('add/', add_teacher, name='add_teacher'),
    path('edit/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('detail/<int:teacher_id>/', teacher_detail, name='teacher_detail'),  # ✅ Teacher Detail Page
]
