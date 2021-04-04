from django.http import HttpResponse
from django.shortcuts import render

def click(request):
    return render(request,'oneclick.html')