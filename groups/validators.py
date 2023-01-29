from django.core.exceptions import ValidationError
from datetime import datetime


def validate_start_date(value):
    start = datetime.strftime(value, '%y-%m-%s')
    current = datetime.strftime(datetime.today(), '%y-%m-%s')
    if start < current:
        raise ValidationError(f"Start date is incorrect")
