import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.validators import ValidateEmailDomain


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    domain = ('gmail.com', 'yahoo.com', 'email.com')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*domain)])
    phone = models.CharField(max_length=19)

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    class Meta:
        abstract = True

    @classmethod
    def _generate(cls):
        f = Faker()
        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthday=f.date_between(start_date='-65y', end_date='-18y'),
            email=f'{first_name}.{last_name}@{f.random.choice(cls.domain)}',
            city=f.city(),
            phone=f.numerify(text='+## (###) ###-##-##')
        )
        obj.save()

        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()
