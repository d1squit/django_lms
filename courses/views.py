from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from courses.forms import UpdateCourseForm, CreateCourseForm
from courses.models import Course
from students.models import Student


@use_args(
    {
        'search': Str(required=False)
    },
    location='query'
)
def get_courses(request, args):
    courses = Course.objects.all().order_by('name')

    if len(args) and args.get('search'):
        courses = courses.filter(
            Q(name__icontains=args.get('search', '')) |
            Q(price__icontains=args.get('search', ''))
        )

    return render(request=request, template_name='courses/list.html', context={'title': 'List of Courses', 'courses': courses})


def detail_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request=request, template_name='courses/detail.html', context={'title': 'Detail of course', 'course': course})


def create_course(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    form = CreateCourseForm()
    return render(request, 'courses/create.html', {'form': form})


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    form = UpdateCourseForm(instance=course)
    return render(request, 'courses/update.html', {'form': form, 'course': course})


def delete_course(request, pk):
    gr = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        gr.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'course': gr})
