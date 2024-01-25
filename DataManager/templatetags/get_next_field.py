from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    try:
        current_index = list(form).index(current_field)
        return form[current_index + 1]
    except (ValueError, IndexError):
        return None