from django.http import HttpResponse

from .models import Student


def index(request):
    students = Student.objects.all().order_by('birthday')
    print(students)
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Birthday</th></tr><thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.birthday}</td></tr>'
    string += '</tbody></table>'
    response = HttpResponse(string)
    return response
