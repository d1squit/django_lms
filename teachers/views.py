from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from teachers.forms import UpdateTeacherForm, CreateTeacherForm
from teachers.models import Teacher


@use_args(
    {
        'search': Str(required=False)
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all().order_by('birthday')

    if len(args) and args.get('search'):
        teachers = teachers.filter(
            Q(first_name__icontains=args.get('search', '')) |
            Q(last_name__icontains=args.get('search', '')) |
            Q(birthday__icontains=args.get('search', '')) |
            Q(salary__icontains=args.get('search', ''))
        )

    return render(request=request, template_name='teachers/list.html', context={'title': 'List of Teachers', 'teachers': teachers})


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request=request, template_name='teachers/detail.html', context={'title': 'Detail of teacher', 'teacher': teacher})


def create_teacher(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'groups/create.html', {'form': form})


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


def delete_teacher(request, pk):
    tr = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        tr.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': tr})
