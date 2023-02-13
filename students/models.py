from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
import datetime

from faker import Faker

from students.validators import ValidateEmailDomain, validate_unique_email

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'email.com')


class Student(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*VALID_DOMAINS), validate_unique_email])
    phone = models.CharField(max_length=19)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def generate_fake_data(cls, amount):
        f = Faker()
        for _ in range(amount):
            st = cls()
            st.first_name = f.first_name()
            st.last_name = f.last_name()
            st.email = f'{st.first_name}.{st.last_name}@{f.random.choice(VALID_DOMAINS)}'
            st.birthday = f.date_between(start_date='-70y', end_date='-18y')
            st.phone = f.numerify(text='+## (###) ###-##-##')
            st.save()
