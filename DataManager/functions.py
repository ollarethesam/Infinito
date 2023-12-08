from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import User

def getkey(dict, value):
    result = None
    for i in dict:
        if value in dict[i]:
            result = i
    return result


def get_form_data(instance):
    field_values = {}

    # Iterate through the fields of the instance
    for field in instance._meta.fields:
        field_name = field.name
        field_value = getattr(instance, field_name)
        # If the field is a ForeignKey, get the related field value
        if isinstance(field, models.ForeignKey) and not isinstance(field, User):
            related_instance = field_value
            if related_instance:
                # Recursively call the function for the related instance
                related_field_values = get_form_data(related_instance)
                # Update the main dictionary with the related field values
                field_values.update({f"{key}": value for key, value in related_field_values.items() if not field_name == 'user'})
        else:
            field_values[field_name] = field_value
    return field_values

def save_or_update(model, modelform, request, pk_val):
    save_msg = 'saved'
    instance = None
    if model.objects.filter(pk=pk_val).exists():
        save_msg = 'updated'
        instance = get_object_or_404(model, pk=pk_val)
    form = modelform(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return JsonResponse({'success': [f'record {instance.pk} {save_msg} succesfully']})
    return JsonResponse({'errors': [error for field, error_list in form.errors.items() for error in error_list]})

def dropdown(model, id, chars, offset, fields):
    if id and not chars:
        fields_values = list(model.objects.values(*fields).order_by(id)[int(offset):int(offset)+20])
        return JsonResponse(fields_values, safe=False)
    if id and chars:
        cond = {f"{id}__contains": chars}
        fields_values = list(model.objects.values(*fields).filter(**cond).order_by(id)[int(offset):int(offset)+20])
        return JsonResponse(fields_values, safe=False)

def formfill(model, key, key_id, keys_list):
    if key and key_id in keys_list[model]:
        values = get_form_data(model.objects.get(pk=key))
        return JsonResponse(values)
    elif key and key_id not in keys_list[model]:
        values = getkey(keys_list, key_id).objects.values(*keys_list[getkey(keys_list, key_id)]).filter(pk=key).first()
        print(values)
        return JsonResponse(values)

def arrows(model, direction, start_value, field):
    first_record = model.objects.values(field).order_by(field).first()[field]
    last_record = model.objects.values(field).order_by(field).last()[field]
    sign = ''
    if direction == 'lt':
        sign = '-'
    if (not start_value or start_value == last_record) and direction == 'gt':
        values = get_form_data(model.objects.order_by(field).first())
    elif (not start_value or start_value == first_record) and direction == 'lt':
        values = get_form_data(model.objects.order_by(field).last())
    else:
        values = get_form_data(model.objects.filter(**{f"{field}__{direction}": start_value}).order_by(f"{sign}{field}").first())
    return JsonResponse(values, safe=False)

def delete(model, delcode):
    if model.objects.filter(pk=delcode).exists():
        model.objects.get(pk=delcode).delete()
        return JsonResponse({'success': [f'record {delcode} deleted succesfully']})
    else:
        return JsonResponse({'errors': [f'record {delcode} doesn\'t exist']})