from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from groups.forms import UpdateGroupForm, CreateGroupForm
from groups.models import Group
from students.models import Student


@use_args(
    {
        'search': Str(required=False)
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all().order_by('name')

    if len(args) and args.get('search'):
        groups = groups.filter(
            Q(name__icontains=args.get('search', '')) |
            Q(start__icontains=args.get('search', '')) |
            Q(description__icontains=args.get('search', ''))
        )

    return render(request=request, template_name='groups/list.html', context={'title': 'List of Groups', 'groups': groups})


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request=request, template_name='groups/detail.html', context={'title': 'Detail of group', 'group': group})


def create_group(request):
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = CreateGroupForm()
    return render(request, 'groups/create.html', {'form': form})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}

    if request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = UpdateGroupForm(instance=group, initial=students)
    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, pk):
    gr = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        gr.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': gr})
