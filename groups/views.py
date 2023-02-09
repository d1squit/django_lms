from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from groups.forms import UpdateGroupForm
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all().order_by('name')
    return render(request=request, template_name='groups/list.html', context={'title': 'List of Groups', 'groups': groups})


def detail_group(request, pk):
    group = Group.objects.get(pk=pk)
    return render(request=request, template_name='groups/detail.html', context={'title': 'Detail of group', 'group': group})


def update_group(request, pk):
    group = Group.objects.get(pk=pk)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
            <a href="/groups/">Back to list</a>
        </form>
        '''

    return HttpResponse(html_form)
