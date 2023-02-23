from django.db import models
from faker import Faker

from core.models import BaseModel
from groups.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    name = models.CharField(max_length=20)
    start = models.DateField(validators=[validate_start_date])
    end = models.DateField()
    description = models.CharField(max_length=100, default='', blank=True)
    headman = models.OneToOneField('students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')
    course = models.OneToOneField('courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='course_group')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Group name: {self.name}'

    @classmethod
    def generate_fake_data(cls, amount):
        f = Faker()
        for _ in range(amount):
            gr = cls()
            gr.name = f.word()
            gr.start = f.date_between(start_date='+1d', end_date='+40d')
            gr.end = f.date_between(start_date='+60d', end_date='+100d')
            gr.save()
