from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from socios.models import usuario
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Porfavor, registre su usuario")

@csrf_exempt
def añadirusuario(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_usuario = usuario(DNI=body['DNI'], numsocio=body['numsocio'], contraseña=body['contraseña'])
    nuevo_usuario.save()
    #body['usuario']
    
    response = {"Info": "correcta"}
    return JsonResponse(response)

@csrf_exempt
def actualizar(request):

    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    actualizar_contra = usuario.objects.filter(DNI=body['DNI'])
    actualizar_contra.update(contraseña = body['contraseña'])
    
    response = {"Info": "correcta"}
    return JsonResponse(response)
@csrf_exempt
def verusuario(request):
    usuarios = list(usuario.objects.values())
    return JsonResponse(usuarios, safe=False)