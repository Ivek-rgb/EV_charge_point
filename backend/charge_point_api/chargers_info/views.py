from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import json
from .charger_manager import ChargerManager

@api_view(['GET', 'POST'])
def process_request(request) -> Response:
    if request.method == 'GET':
        print("GET Request zaprimljen")
        return Response({"porukica" : "Pozdrav svijete!"})
    elif request.method == 'POST':
        pass

@api_view(['GET'])
def process_charger_request_id(request, charger_id): 
    cm = ChargerManager() 
    return cm.handle_charger_available(charger_id)
        
def get_chargers(): 
    pass