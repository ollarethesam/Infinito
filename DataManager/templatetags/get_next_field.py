from django import template

register = template.Library()

@register.filter
def get_next_field(form, current_field):
    form_fields = list(form)
    current_index = form_fields.index(current_field)
    print(current_index)
    return current_index
