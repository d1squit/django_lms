from django.core.exceptions import ValidationError
from datetime import datetime


def validate_start_date(value):
    print(value)
    start = datetime.strftime(value, '%y-%m-%d')
    current = datetime.strftime(datetime.today(), '%y-%m-%d')
    if start < current:
        raise ValidationError(f"Start date is incorrect")
