from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    try:
        form_fields = form.fields.items()
        current_index = list(form_fields).index((current_field.name, current_field))
        return form[current_index + 1]
    except (ValueError, IndexError):
        print(form_fields)
        return None
