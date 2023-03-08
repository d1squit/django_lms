from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        students = Student.objects.all().order_by('birthday').select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)
        return filter_form


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = CreateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
