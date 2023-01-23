from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20)
    start = models.DateField()
    description = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'
