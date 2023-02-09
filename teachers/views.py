from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from teachers.forms import UpdateTeacherForm
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all().order_by('birthday')
    return render(request=request, template_name='teachers/list.html', context={'title': 'List of Teachers', 'teachers': teachers})


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request=request, template_name='teachers/detail.html', context={'title': 'Detail of teacher', 'teacher': teacher})


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/update.html', {'form': form})
