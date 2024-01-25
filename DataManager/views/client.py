from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.ClientForm import ClientForm
from DataManager.models.client import Client
from django.shortcuts import get_object_or_404
from ..functions import *
from .banche import Banche
from .modpag import Modpag
from .zone import   Zone
from .eseiva import Eseiva
from .valute import Valute
from .nazion import Nazion
from .catego import Catego
from .ivaven import Ivaven

def client(request, model=Client, modelform=ClientForm, template='DataManager/mainform.html', url_name='client', keys_list={
    Client: ('codcli', 'ragsoc'),
    Banche:('codban', 'desban'),
    Modpag:('codpag', 'despag'),
    Zone : ('codzon', 'deszon'),
    Eseiva:('codese', 'datric'),
    Valute:('codval', 'desval'),
    Nazion:('codnaz', 'desnaz'),
    Catego:('codcat', 'descat'),
    Ivaven:('codiva', 'desiva') 
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
        if id:
            return dropdown(getkey(keys_list, id), id, chars, offset, keys_list[getkey(keys_list, id)])
        
        key = request.GET.get("key")
        key_id = request.GET.get("key_id")
        from_input = request.GET.get("from_input")
        if key and key_id:
            return formfill(model, key, key_id, keys_list, from_input=from_input)
        
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