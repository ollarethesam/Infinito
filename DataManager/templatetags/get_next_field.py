from django import template

register = template.Library()

@register.filter
def get_next_field(form, field):
    try:
        keys = list(form.fields.keys())
        index = keys.index(field.name)
        i = 1
        next_field_name = keys[index + 1]
        no_label_fields = []
        while not form[next_field_name].label:
            no_label_fields.append(form[next_field_name])
            next_field_name = keys[index + i]
            i += 1
        return no_label_fields
    except (ValueError, IndexError):
        return ''
