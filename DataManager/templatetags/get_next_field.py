from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    try:
        form_fields = list(form)
        current_index = form_fields.index(current_field)
        return form[form_fields[current_index + 1]]
    except (ValueError, IndexError) as e:
        print(form_fields)
        print(e)
        return None
