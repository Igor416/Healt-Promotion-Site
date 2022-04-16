from health.settings import HOST
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'home': True,
        'host': HOST,
        'title': 'Главная'
    }
    return render(request, 'home.html', context=context)

def alcohol(request):
    context = {
        'home': False,
        'host': HOST,
        'title': 'Алкозависимость'
    }
    return render(request, 'alcohol.html', context=context)

def smoking(request):
    context = {
        'home': False,
        'host': HOST,
        'title': 'Курение'
    }
    return render(request, 'smoking.html', context=context)

def drugs(request):
    context = {
        'home': False,
        'host': HOST,
        'title': 'Наркозависимость'
    }
    return render(request, 'drugs.html', context=context)
