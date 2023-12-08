from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.DestfoForm import DestfoForm
from DataManager.models.destfo import Destfo
from DataManager.models.fornit import Fornit
from django.shortcuts import get_object_or_404
from ..functions import *

def destfo(request, model=Destfo, modelform=DestfoForm, template='DataManager/mainform.html', url_name='destfo', keys_list={
    Destfo: ('codest', 'dedest'),
    Fornit: ('codfor', 'ragsoc') 
}):
    
    if request.method == 'POST':   
        pk_val = request.POST[model._meta.pk.name]
        return save_or_update(model, modelform, request, pk_val)
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name, 'ddfields': ('codest', 'dedest', 'codfor', 'ragsoc'), 'ddofields': {'codcli': 'Fornitori'}}

        id = request.GET.get('id')
        offset = request.GET.get('offset')
        chars = request.GET.get('chars')
        if id and id in keys_list[model]:
            return dropdown(model, id, chars, offset, keys_list[model])
        elif id and not id in keys_list[model]:
            return dropdown(getkey(keys_list, id), id, chars, offset, keys_list[getkey(keys_list, id)])
        
        key = request.GET.get("key")
        key_id = request.GET.get('key_id')
        if key:
            return formfill(model, key, key_id, keys_list)
        
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