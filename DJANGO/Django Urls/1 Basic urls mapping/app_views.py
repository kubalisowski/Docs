from django.shortcuts import render

def index(request):
    return render(request, 'basicapp/index.html')

def other(request):
    return render(request, 'basicapp/other.html')

def relative(request):
    return render(request, 'basicapp/relative.html')