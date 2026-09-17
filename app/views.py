from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
	return render(request,'home.html')

def produtos_view(request):
    return render(request,'products.html')
