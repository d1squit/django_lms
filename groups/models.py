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

    @classmethod
    def generate_fake_data(cls, amount):
        f = Faker()
        for _ in range(amount):
            st = cls()
            st.first_name = f.first_name()
            st.last_name = f.last_name()
            st.birthday = f.date_between(start_date='-70y', end_date='-18y')
            st.salary = f.random.randint(800, 4000)
            st.save()
