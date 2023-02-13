from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404

from groups.forms import UpdateGroupForm
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all().order_by('name')
    return render(request=request, template_name='groups/list.html', context={'title': 'List of Groups', 'groups': groups})


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request=request, template_name='groups/detail.html', context={'title': 'Detail of group', 'group': group})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(request, 'groups/update.html', {'form': form})
