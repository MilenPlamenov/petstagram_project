from django.core.exceptions import ValidationError


def clean_fields_factory(input_from_field, field_name):
    if len(input_from_field) < 2:
        raise ValidationError(f'{field_name.capitalize()} minimum length is 2 characters!')
    elif len(input_from_field) > 30:
        raise ValidationError(f'{field_name.capitalize()} maximum length is 30 characters!')