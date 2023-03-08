from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from teachers.forms import CreateTeacherForm, UpdateTeacherForm
from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
