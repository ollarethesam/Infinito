from django import template

register = template.Library()

@register.filter
def get_next_field(form, field):
    try:
        keys = list(form.fields.keys())
        index = keys.index(field.name)
        next_field_name = keys[index + 1]
        return form[next_field_name]
    except (ValueError, IndexError):
        return None
