from django import template

register = template.Library()

@register.filter
def get_next_field(form_fields, current_field_name):
    try:
        keys = list(form_fields.keys())
        current_index = keys.index(current_field_name)
        next_field_name = keys[current_index + 1]
        print(form_fields)
        return form_fields[next_field_name]
    except (ValueError, IndexError):
        return None
