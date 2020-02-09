from django.shortcuts import render
from uploaddownload.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def api_data(request):
    foods = food.objects.all()
    dict_value = {"foods": list(foods.values("title","name"))}
    return JsonResponse(dict_value)  

def api_spec_data(request,pk=None):
    foods = food.objects.get(pk=pk)
    return JsonResponse({"title" : foods.title, "name" : foods.name})  


@csrf_exempt 
def api_add(request):
    foods = food()
    if request.method == "POST":
        decoded_data = request.body.decode('utf-8')
        food_data = json.loads(decoded_data)
        foods.title = food_data['title']
        foods.name = food_data['name']
        foods.save()
        return JsonResponse({"message" : "Completed"})
    else:
        return JsonResponse({"title" : foods.title, "name" : foods.name})
    
        
@csrf_exempt        
def api_update_data(request, pk=None):
    foods = food.objects.get(pk=pk)
    if request.method == "PUT":
        decoded_data = request.body.decode('utf-8')
        food_data = json.loads(decoded_data)
        foods.title = food_data['title']
        foods.name = food_data['name']
        foods.save()
        return JsonResponse({"message" : "Updated"})
    
    else:
       return JsonResponse({"title" : foods.title, "name" : foods.name})
    
@csrf_exempt        
def api_delete_data(request, pk=None):
    foods = food.objects.get(pk=pk)
    if request.method == "DELETE":
        foods.delete()
        return JsonResponse({"message" : "Deleted"})
    
    else:
        return JsonResponse({"title" : foods.title, "name" : foods.name})
    
