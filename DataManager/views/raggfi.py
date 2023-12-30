from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.RaggfiForm import RaggfiForm
from DataManager.models.raggfi import Raggfi
from django.shortcuts import get_object_or_404
from ..functions import *

def raggfi(request, model=Raggfi, modelform=RaggfiForm, template='DataManager/mainform.html', url_name='raggfi'):
    if request.method == 'POST':   
        pk_val = request.POST[model._meta.pk.name]
        return save_or_update(model, modelform, request, pk_val)
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name, 'ddfields': ('codrag', 'desrag')}

        id = request.GET.get('id')
        offset = request.GET.get('offset')
        chars = request.GET.get('chars')
        if id:
            return dropdown(model, id, chars, offset, context['ddfields'])
        
        key = request.GET.get("key")
        key_id = request.GET.get("key_id")
        from_input = request.GET.get("from_input")
        if key and key_id:
            return formfill(model, key, key_id, {model: context['ddfields']}, from_input=from_input)
        
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