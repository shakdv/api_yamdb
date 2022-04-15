from datetime import date
from django.core.exceptions import ValidationError


def year_validator(value):
    if value > date.today().year:
        raise ValidationError(
            'Нельзя добавлять произведения, которые еще не вышли!'
        )
