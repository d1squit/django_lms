from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    name = models.CharField(max_length=20)
    start = models.DateField(validators=[validate_start_date])
    description = models.CharField(max_length=100, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'
