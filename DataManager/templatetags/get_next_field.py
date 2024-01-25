from django import template

register = template.Library()

@register.filter
def get_next_field(form, field):
    index = form[field.name]
    return index
