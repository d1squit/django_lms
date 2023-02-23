from django.core.validators import MinLengthValidator
from django.db import models
import datetime

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.date.today)
    salary = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_fake_data(cls, amount):
        f = Faker()
        for _ in range(amount):
            tr = cls()
            tr.first_name = f.first_name()
            tr.last_name = f.last_name()
            tr.birthday = f.date_between(start_date='-70y', end_date='-18y')
            tr.salary = f.random.randint(800, 4000)
            tr.save()
