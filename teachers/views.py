from django.shortcuts import render, redirect, get_object_or_404

from .forms import TeacherForm
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()  # Fetch all teachers from the database

    return render(request, 'teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

def edit_teacher(request, teacher_id):
    teacher = (
        get_object_or_404(Teacher, id=teacher_id))
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_form.html', {'form': form})

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teacher_confirm_delete.html', {'teacher': teacher})


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})