from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def getkey(dict, value):
    result = None
    for i in dict:
        if value in dict[i]:
            result = i
    return result


def get_form_data(instance, fields=None):
    field_values = {}
    # Iterate through the fields of the instance
    for field in instance._meta.fields:
        field_name = field.name
        if fields is not None and field_name not in fields or field_name == 'date_created':
            continue

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

def save_or_update(model, modelform, request, pk_vals):
    save_msg = 'saved'
    instance = None
    if not isinstance(pk_vals, dict):
        cond = {model._meta.pk.name: pk_vals}
    else:
        cond = pk_vals
    if model.objects.filter(**cond).exists():
        save_msg = 'updated'
        instance = get_object_or_404(model, **cond)
    form = modelform(request.POST or None, instance=instance)
    try:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date_created = datetime.now()
            instance.save()
            return JsonResponse({'success': [f'record {instance.pk} {save_msg} succesfully']})
        return JsonResponse({'errors': [error for field, error_list in form.errors.items() for error in error_list]})
    except Exception as e:
        print(e)
        return JsonResponse({'errors': [f'{e}']})
    
def dropdown(model, id, chars, offset, fields):
    if id and not chars:
        fields_values = list(model.objects.values(*fields).order_by(id)[int(offset):int(offset)+20])
        return JsonResponse(fields_values, safe=False)
    if id and chars:
        cond = {f"{id}__contains": chars}
        fields_values = list(model.objects.values(*fields).filter(**cond).order_by(id)[int(offset):int(offset)+20])
        return JsonResponse(fields_values, safe=False)

def formfill(model, key, key_id, keys_list, grid=False, grid_keys=None, main=None, from_input=False):
    try:
        cond = {key_id: key}
        if key and key_id in keys_list[model]:
            if from_input:
                values = get_form_data(model.objects.get(**cond))
            else:
                values = get_form_data(model.objects.get(pk=key))
        elif key and key_id not in keys_list[model]:
            values = getkey(keys_list, key_id).objects.values(*keys_list[getkey(keys_list, key_id)]).filter(pk=key).first()
        if grid and grid_keys and key_id == main:
            instances = list(model.objects.filter(**cond))
            values['grid'] = []
            for instance in instances:
                values['grid'].append(get_form_data(instance, fields=grid_keys))
        return JsonResponse(values)
    except model.DoesNotExist as e:
        print(e, type(e))
        return JsonResponse({'grid':{}})
    except TypeError as e:
        print(e, type(e))
        return JsonResponse({'grid':{}})

def arrows(model, direction, start_value, field, fields=None, grid=False, grid_keys=None, main=None):
    first_record = model.objects.values(field).order_by(field).first()[field]
    last_record = model.objects.values(field).order_by(field).last()[field]
    sign = ''
    if direction == 'lt':
        sign = '-'
    if (not start_value or start_value == last_record) and direction == 'gt':
        instance = model.objects.order_by(field).first()
    elif (not start_value or start_value == first_record) and direction == 'lt':
        instance = model.objects.order_by(field).last()
    else:
        instance = model.objects.filter(**{f"{field}__{direction}": start_value}).order_by(f"{sign}{field}").first()
    values = get_form_data(instance, fields)
    if grid and grid_keys:
            cond = {main: getattr(instance, main, None)}
            instances = list(model.objects.filter(**cond))
            values['grid'] = []
            for instance in instances:
                values['grid'].append(get_form_data(instance, fields=grid_keys))
            print(values['grid'])
    return JsonResponse(values)

def delete(model, delcode, delkeys=None):

    if not isinstance(delcode, dict):
        cond = {model._meta.pk.name: delcode}
    else:
        cond = delcode
    print(cond)
    if model.objects.filter(**cond).exists():
        try:
            model.objects.get(**cond).delete()
            return JsonResponse({'success': [f'record {delcode} deleted succesfully']})
        except Exception as e:
            print(e)
            return JsonResponse({'errors': [f'the record {delcode} is connected to other tables']})
    else:
        return JsonResponse({'errors': [f'record {delcode} doesn\'t exist']})