
# Create your views here.
from django.shortcuts import render, redirect
from .forms import Ourform
from .models import food
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt


def uploadfiles(request):
    if request.method == "POST":
        form = Ourform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploaddownload:list_food')


    form = Ourform()
    return render(request, 'uploaddownload/food.html',
            {'form' : form})

def list_food(request):
	alu = food.objects.all()
	query=""
	if request.GET:
		query = request.GET['q']
	alu = get_data_queryset(str(query))
	return render(request, "uploaddownload/y.html", {"food":alu})


def get_data_queryset(query=None):
	queryset=[]
	queries = query.split(" ") #split: this will convert the strings into list
	for q in queries:
		alu = food.objects.filter(
		Q(title__icontains=q) |
		Q(name__icontains=q)
		)

		for foods in alu:
			queryset.append(foods)

	return list(set(queryset))  #typecasting: changing the type of a variable.

def delete_data(request, pk):
	alu = food.objects.get(pk=pk)
	alu.delete()
	return redirect('uploaddownload:list_food')