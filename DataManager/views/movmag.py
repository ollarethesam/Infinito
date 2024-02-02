from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.MovmagForm import MovmagForm
from models.movmag import Movmag
from models.caumag import Caumag
from models.client import Client
from models.fornit import Fornit
from models.artico import Artico
from models.commes import Commes
from django.shortcuts import get_object_or_404
from ..functions import *

def movmag(request, model=Movmag, modelform=MovmagForm, template='DataManager/mainform.html', url_name='movmag', keys_list={
    Movmag: ('numpro', 'datmov'),
    Caumag: ('codcau', 'descau'),
    Client: ('codcli', 'ragsoc'),
    Fornit: ('codfor', 'ragsoc'),
    Artico: ('codart', 'desart'),
    Commes: ('codcom', 'descom')
}):
    
    if request.method == 'POST':   
        pk_vals = (request.POST[model._meta.numpro], request.POST[model._meta.anno])
        save_msg = 'saved'
        instance = None
        cond = {'numpro': pk_vals[0], 'anno':pk_vals[1]}
        if model.objects.filter(**cond).exists():
            save_msg = 'updated'
            instance = get_object_or_404(model, **cond)
        form = modelform(request.POST or None, instance=instance)
        try:
            if form.is_valid():
                anno = form.cleaned_data['anno']
                instance = form.save(commit=False)
                instance.numpro = model.objects.filter(anno=anno).last().numpro + 1
                instance.user = request.user
                instance.save()
                return JsonResponse({'success': [f'record {instance.pk} {save_msg} succesfully']})
            return JsonResponse({'errors': [error for field, error_list in form.errors.items() for error in error_list]})
        except Exception as e:
            print(e)
            return JsonResponse({'errors': [f'{e}']})
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name, 'ddfields': ('numpro'), 'ddofields': {'codcli': 'Clienti'}}

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