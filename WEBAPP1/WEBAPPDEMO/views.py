from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def food(request):
    return render(request, 'WEBAPP1/base.html')