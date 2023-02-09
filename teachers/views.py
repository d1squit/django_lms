from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

from teachers.forms import UpdateTeacherForm
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all().order_by('birthday')
    return render(request=request, template_name='teachers/list.html', context={'title': 'List of Teachers', 'teachers': teachers})


def detail_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request=request, template_name='teachers/detail.html', context={'title': 'Detail of teacher', 'teacher': teacher})


def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
            <a href="/teachers/">Back to list</a>
        </form>
        '''

    return HttpResponse(html_form)
