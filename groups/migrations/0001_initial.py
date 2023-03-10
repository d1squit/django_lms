# Generated by Django 4.1.5 on 2023-02-23 16:22

from django.db import migrations, models
import groups.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('start', models.DateField(validators=[groups.validators.validate_start_date])),
                ('end', models.DateField()),
                ('description', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
