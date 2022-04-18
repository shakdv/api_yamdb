from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    current_year = timezone.now().year
    if value > current_year:
        raise ValidationError(
            'Нельзя добавлять произведения, которые еще не вышли!'
        )


def username_validator(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Имя пользователя не может быть "me".',
            params={'value': value},
        )
