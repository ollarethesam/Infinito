from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    form_keys = list(form.fields.items.keys())
    try:
        current_index = form_keys.index(current_field.name)
        next_field_name = form_keys[current_index + 1]
        return form.fields.items[next_field_name]
    except (ValueError, IndexError):
        return None
