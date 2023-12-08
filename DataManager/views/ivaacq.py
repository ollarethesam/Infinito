from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.IvaacqForm import IvaacqForm
from DataManager.models.ivaacq import Ivaacq
from django.shortcuts import get_object_or_404
from ..functions import *

def ivaacq(request, model=Ivaacq, modelform=IvaacqForm, template='DataManager/mainform.html', url_name='ivaacq'):
    if request.method == 'POST':   
        pk_val = request.POST[model._meta.pk.name]
        return save_or_update(model, modelform, request, pk_val)
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name, 'ddfields': ('codiva', 'desiva')}

        id = request.GET.get('id')
        offset = request.GET.get('offset')
        chars = request.GET.get('chars')
        if id:
            return dropdown(model, id, chars, offset, context['ddfields'])
        
        key = request.GET.get("key")
        if key:
            values = model.objects.filter(pk=key).values().first()
            return JsonResponse(values)
        
        direction = request.GET.get('direction')
        start_value = request.GET.get('start_value')
        field = request.GET.get('field')
        if direction:
            return arrows(model, direction, start_value, field)
                
        delcode = request.GET.get('delcode')
        if delcode:
            return delete(model, delcode)
        content = render(request, template, context)
        return HttpResponse(content)