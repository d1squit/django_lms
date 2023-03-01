from random import choice

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
import datetime

from faker import Faker

from core.models import PersonModel
from groups.models import Group
from core.validators import ValidateEmailDomain, validate_unique_email

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'email.com')


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        groups = Group.objects.all()
        student = super()._generate()
        student.group = choice(groups)
        student.save()
