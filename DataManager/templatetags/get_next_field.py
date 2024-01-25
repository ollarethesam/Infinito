from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    try:
        form_fields = list(form)
        current_index = form_fields.index(current_field)
        print(form_fields)
        return form[form_fields[current_index + 1]]
    except (ValueError, IndexError) as e:
        return None
