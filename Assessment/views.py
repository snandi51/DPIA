from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def screening(request):
    return render(request, 'screening.html')

def temp(request):
    return render(request, 'temp.html')


def dpia_screening(request):
    return render(request, 'dpia_screening.html')


def risk_summary(request):
    return render(request, 'risk_summary.html')


def heat_map(request):
    return render(request, 'heat_map.html')


