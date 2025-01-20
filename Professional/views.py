from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
@csrf_exempt
@require_POST
def register(request):
    dado = json.loads(request.body)
    print(dado)
    return JsonResponse({'register' :  'register'})

# Create your views here.
