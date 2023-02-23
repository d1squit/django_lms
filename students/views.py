from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


@use_args(
    {
        'search': Str(required=False)
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all().order_by('birthday').select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    # if len(args) and args.get('search'):
    #     students = students.filter(
    #         Q(first_name__icontains=args.get('search', '')) |
    #         Q(last_name__icontains=args.get('search', '')) |
    #         Q(email__icontains=args.get('search', '')) |
    #         Q(birthday__icontains=args.get('search', '')) |
    #         Q(phone__icontains=args.get('search', ''))
    #     )

    return render(request=request, template_name='students/list.html', context={'filter_form': filter_form})


def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request=request, template_name='students/detail.html', context={'title': 'Detail of student', 'student': student})


def create_student(request):
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    form = CreateStudentForm()
    return render(request, 'students/create.html', {'form': form})


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


def delete_student(request, pk):
    st = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': st})
