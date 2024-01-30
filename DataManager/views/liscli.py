from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.LiscliForm import LiscliForm
from DataManager.models.artico import Artico
from DataManager.models.client import Client
from DataManager.models.liscli import Liscli
from django.shortcuts import get_object_or_404
from ..functions import *

def liscli(request, model=Liscli, modelform=LiscliForm, template='DataManager/mainform.html', url_name='liscli', keys_list={
    Liscli: (),
    Artico: ['codart', 'desart', 'prezzo'],
    Client: ('codcli', 'ragsoc') 
}):
    
    if request.method == 'POST':   
        pk_vals = {'codcli': request.POST['codcli'],
                   'codart': request.POST['codart']
        } 
        return save_or_update(model, modelform, request, pk_vals)
    
    if request.method == 'GET':
        form = modelform
        context = {
                'form': form,
                'url_name': url_name,
                'ddfields': ('codart', 'desart', 'codcli', 'ragsoc'),
                'ddofields': {'codcli': 'Clienti', 'codart': 'Gestione-Articoli'},
                'grid':{'codart': 'Articolo','desart': 'Descrizione','prezzo': 'Prezzo'}
            }
        main = 'codcli'

        id = request.GET.get('id')
        offset = request.GET.get('offset')
        chars = request.GET.get('chars')
        if id and id in keys_list[model]:
            return dropdown(model, id, chars, offset, keys_list[model])
        elif id and not id in keys_list[model]:
            return dropdown(getkey(keys_list, id), id, chars, offset, keys_list[getkey(keys_list, id)][:2])
        
        key = request.GET.get("key")
        key_id = request.GET.get('key_id')
        grid = request.GET.get('grid')
        if key:
            grid_keys = tuple(context['grid'].keys())
            print(grid_keys)
            return formfill(model, key, key_id, keys_list, grid=grid, grid_keys=grid_keys, main=main)
        
        grid_pk_value = request.GET.get('grid_pk_value')
        grid_pk_name = request.GET.get('grid_pk_name')
        main_val = request.GET.get('main_val')
        if grid_pk_value:
            data = get_form_data(model.objects.get(**{grid_pk_name: grid_pk_value, main: main_val}), fields=keys_list[Artico])
            return JsonResponse(data)
        
        direction = request.GET.get('direction')
        start_value = request.GET.get('start_value')
        field = main
        if direction:
            grid_keys = tuple(context['grid'].keys())
            return arrows(model, direction, start_value, field, fields=keys_list[getkey(keys_list, main)], grid=grid, grid_keys=grid_keys, main=main)
                
        delcode = request.GET.get('delcode')
        if delcode:
            return delete(model, delcode)
        
        content = render(request, template, context)
        return HttpResponse(content)