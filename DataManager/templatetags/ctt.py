from django import template

register = template.Library()

@register.simple_tag
def get_prev_field(form, index):
    return form[index - 1]

@register.filter
def field_has_label(field):
    return bool(field.label)