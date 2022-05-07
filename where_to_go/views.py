from django.http import HttpResponse
from django.shortcuts import render



def show_maps(request):
    return render(request, 'product_page.html')
