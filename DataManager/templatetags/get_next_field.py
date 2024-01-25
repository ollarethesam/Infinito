from django import template

register = template.Library()

@register.filter
def get_next_field(form_fields, current_field_name):
    form_keys = list(form_fields.keys())
    try:
        current_index = form_keys.index(current_field_name)
        next_field_name = form_keys[current_index + 1]
        return form_fields[next_field_name]
    except (ValueError, IndexError):
        print(next_field_name)
        return None
