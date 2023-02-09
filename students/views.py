from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm, UpdateStudentForm
from .models import Student
from .utils import format_list_student


def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False)
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all().order_by('birthday')

    if len(args) and (args.get('first_name') or args.get('last_name')):
        students = students.filter(
            Q(first_name__icontains=args.get('first_name', '')) &
            Q(last_name__icontains=args.get('last_name', ''))
        )

    return render(request=request, template_name='students/list.html', context={'title': 'List of Students', 'students': students})


def detail_student(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request=request, template_name='students/detail.html', context={'title': 'Detail of student', 'student': student})


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
            <a href="/students/">Back to list</a>
        </form> 
        '''

    return HttpResponse(html_form)


def update_student(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
            <a href="/students/">Back to list</a>
        </form>
        '''

    return HttpResponse(html_form)
