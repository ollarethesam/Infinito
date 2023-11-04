from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from DataManager.forms.BancheForm import BancheForm
from DataManager.models.banche import Banche
from django.shortcuts import get_object_or_404


def banche(request, model=Banche, modelform=BancheForm, template='DataManager/mainform.html', url_name='banche'):
    if request.method == 'POST':   
        instance = None
        pk_val = request.POST[model._meta.pk.name]
        if model.objects.filter(pk=pk_val).exists():
            instance = get_object_or_404(model, pk=pk_val)
        form = modelform(request.POST or None, instance=instance)
        context = {'form': form, 'url_name': url_name}
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return JsonResponse({'success': [f'record {instance.pk} saved succesfully']})
        return JsonResponse({'errors': [error for field, error_list in form.errors.items() for error in error_list]})
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name, 'ddfields': ('codban', 'desban')}

        id = request.GET.get('id')
        chars = request.GET.get('chars')
        if id and not chars:
            fields_values = list(model.objects.values(*context['ddfields']).order_by(id))
            return JsonResponse(fields_values, safe=False)
        if id and chars:
            cond = {f"{id}__contains": chars}
            fields_values = list(model.objects.values(*context['ddfields']).filter(**cond).order_by(id))
            return JsonResponse(fields_values, safe=False)
        
        key = request.GET.get("key")
        if key:
            values = model.objects.filter(pk=key).values().first()
            return JsonResponse(values)
        
        direction = request.GET.get('direction')
        start_value = request.GET.get('start_value')
        field = request.GET.get('field')
        if direction:
            first_record = model.objects.values(field).order_by(field).first()[field]
            last_record = model.objects.values(field).order_by(field).last()[field]
            sign = ''
            if direction == 'lt':
                sign = '-'
            values = model.objects.filter(**{f"{field}__{direction}": start_value}).order_by(f"{sign}{field}").values().first()
            if (not start_value or start_value == last_record) and direction == 'gt':
                values = model.objects.values().order_by(field).first()
            if (not start_value or start_value == first_record) and direction == 'lt':
                values = model.objects.values().order_by(field).last()
            return JsonResponse(values, safe=False)
                
        delcode = request.GET.get('delcode')
        if delcode:
            if model.objects.filter(pk=delcode).exists():
                model.objects.get(pk=delcode).delete()
                return JsonResponse({'success': [f'record {delcode} deleted succesfully']})
            else:
                return JsonResponse({'errors': [f'record {delcode} doesn\'t exist']})
        content = render(request, template, context)
        return HttpResponse(content)