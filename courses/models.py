from django.db import models
from faker import Faker

from core.models import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(default=5_000)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def generate_fake_data(cls, amount):
        f = Faker()
        for _ in range(amount):
            gr = cls()
            gr.name = f.word()
            gr.price = f.random.randint(4000, 15000)
            gr.save()