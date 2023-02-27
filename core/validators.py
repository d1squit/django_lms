from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

DOMAINS = ('gmail.com', 'yahoo.com')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        self.domains = tuple(domains) if domains else DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f"Email's domain '{domain}' is not correct")


def validate_unique_email(value):
    from students.models import Student
    students = Student.objects.filter(email=value)
    if len(students) > 0:
        raise ValidationError(f"User with this email already exists")
