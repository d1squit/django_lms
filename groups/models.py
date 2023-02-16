from django.db import models
from faker import Faker

from groups.validators import validate_start_date


class Group(models.Model):
    name = models.CharField(max_length=20)
    start = models.DateField(validators=[validate_start_date])
    description = models.CharField(max_length=100, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
            gr.save()
