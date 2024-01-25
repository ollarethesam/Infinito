from django import template

register = template.Library()

@register.simple_tag
def get_next_field(form, index):
    return form[index + 1] if index + 1 < form|length else None