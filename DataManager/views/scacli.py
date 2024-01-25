from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.ScacliForm import ScacliForm
from DataManager.models.scacli import Scacli
from django.shortcuts import get_object_or_404
from ..functions import *
from .banche import Banche
from .modpag import Modpag
from .valute import Valute
from .client import Client

def scacli(request, model=Scacli, modelform=ScacliForm, template='DataManager/mainform.html', url_name='scacli', keys_list={
    Scacli: ('numpro', 'descri'),
    Client: ('codcli', 'ragsoc'),
    Banche:('codban', 'desban'),
    Modpag:('codpag', 'despag'),
    Valute:('codval', 'desval'),
}):
    
    if request.method == 'POST':   
        pk_val = request.POST[model._meta.pk.name]
        return save_or_update(model, modelform, request, pk_val)
    if request.method == 'GET':
        form = modelform
        context = {'form': form,
                'url_name': url_name,
                'ddfields': (
                    'numpro',
                    'descri',
                    'codcli',
                    'ragsoc',
                    'codval',
                    'desval',
                    'codpag',
                    'despag',
                    'codban',
                    'desban'
                ),
                'ddofields': {
                    'codcli': 'Clienti',
                    'codban': 'Gestione-Tabella-Banche',
                    'codpag': 'Modalita-di-Pagamento',
                    'codval': 'Valute',
                }}

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