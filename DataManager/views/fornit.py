from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.FornitForm import FornitForm
from DataManager.models.fornit import Fornit
from DataManager.models.banche import Banche
from DataManager.models.nazion import Nazion
from DataManager.models.catego import Catego
from DataManager.models.modpag import Modpag
from DataManager.models.ivaacq import Ivaacq
from DataManager.models.zone import Zone
from django.shortcuts import get_object_or_404
from ..functions import *

def fornit(request, model=Fornit, modelform=FornitForm, template='DataManager/fornit.html', url_name='fornit', keys_list={
    Fornit: ('codfor', 'ragsoc'),
    Banche:('codban', 'desban'),
    Modpag:('codpag', 'despag'),
    Zone : ('codzon', 'deszon'),
    Nazion:('codnaz', 'desnaz'),
    Catego:('codcat', 'descat'),
    Ivaacq:('codiva', 'desiva') 
}):
    
    if request.method == 'POST':   
        pk_val = request.POST[model._meta.pk.name]
        return save_or_update(model, modelform, request, pk_val)
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name}

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