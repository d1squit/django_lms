from django.core.exceptions import ValidationError

DOMAINS = ('gmail.com', 'yahoo.com')


def validate_email_domain(value):
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError(f"Email's domain '{domain}' is not correct")


def validate_unique_email(value):
    from students.models import Student
    students = Student.objects.filter(email=value)
    if len(students) > 0:
        raise ValidationError(f"User with this email already exists")
