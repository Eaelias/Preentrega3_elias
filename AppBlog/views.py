from django.http import HttpResponse
from django.shortcuts import render

def show_html(request):
    context = {}
    return render(request, 'index.html', context)

