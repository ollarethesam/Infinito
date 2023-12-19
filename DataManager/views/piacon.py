from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from DataManager.forms.PiaconForm import PiaconForm
from DataManager.models.piacon import Piacon
from DataManager.models.conabi import Conabi
from django.shortcuts import get_object_or_404
from ..functions import *

def piacon(request, model=Piacon, modelform=PiaconForm, template='DataManager/mainform.html', url_name='piacon', keys_list={
    Piacon: ('codpia', 'despia'),
    Conabi: ('codcon', 'descon') 
}):
    
    if request.method == 'POST':   
        pk_val = request.POST[model._meta.pk.name]
        save_msg = 'saved'
        instance = None
        conabi_instance = None
        if model.objects.filter(pk=pk_val).exists():
            save_msg = 'updated'
            instance = get_object_or_404(model, pk=pk_val)
            conabi_instance = Conabi.objects.get(pk=pk_val)
        form = modelform(request.POST or None, instance=instance)
        if form.is_valid():
            if conabi_instance:
                conabi_instance.descon = form.cleaned_data['despia']
                conabi_instance.save()
            instance = form.save(commit=False)
            instance.user = request.user
            if not Conabi.objects.filter(pk=pk_val).exists():
                conabi = Conabi(codcon=instance.codpia, descon=instance.despia, user=request.user)
                conabi.save()
            else:
                print(form.cleaned_data)
                if not form.cleaned_data['decoab'] and form.cleaned_data['codcon']:
                    conabi = Conabi.objects.get(pk=request.POST['codcon'])
                    instance.codcon = conabi
                else:
                    instance.codcon = None
            instance.save()
            return JsonResponse({'success': [f'record {instance.pk} {save_msg} succesfully']})
        return JsonResponse({'errors': [error for field, error_list in form.errors.items() for error in error_list]})
    if request.method == 'GET':
        form = modelform
        context = {'form': form, 'url_name': url_name, 'ddfields': ('codpia', 'despia', 'codcon', 'descon')}

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
            if model.objects.filter(pk=delcode).exists():
                model.objects.get(pk=delcode).delete()
                Conabi.objects.get(pk=delcode).delete()
                return JsonResponse({'success': [f'record {delcode} deleted succesfully']})
            else:
                return JsonResponse({'errors': [f'record {delcode} doesn\'t exist']})
        
        content = render(request, template, context)
        return HttpResponse(content)