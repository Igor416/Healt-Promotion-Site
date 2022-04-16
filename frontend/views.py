from health.settings import HOST
from django.shortcuts import render

# Create your views here.
def create_css_file(name):
    return 'css/' + name + '.css'

def home(request):
    context = {
        'home': True,
        'host': HOST,
        'css_name': create_css_file('home'),
        'title': 'Главная'
    }
    return render(request, 'home.html', context=context)

def alcohol(request):
    context = {
        'home': False,
        'host': HOST,
        'css_name': create_css_file('alcohol'),
        'title': 'Алкозависимость'
    }
    return render(request, 'alcohol.html', context=context)

def smoking(request):
    context = {
        'home': False,
        'host': HOST,
        'css_name': create_css_file('smoking'),
        'title': 'Курение'
    }
    return render(request, 'smoking.html', context=context)

def drugs(request):
    context = {
        'home': False,
        'host': HOST,
        'css_name': create_css_file('drugs'),
        'title': 'Наркозависимость'
    }
    return render(request, 'drugs.html', context=context)
