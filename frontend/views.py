from health.settings import HOST
from django.shortcuts import render

# Create your views here.
def create_file_name(name, ext):
    return f'{ext}/{name}.{ext}'

def home(request):
    context = {
        'home': True,
        'host': HOST,
        'css_name': create_file_name('home', 'css'),
        'js_name': create_file_name('home', 'js'),
        'title': 'Главная'
    }
    return render(request, 'home.html', context=context)

def alcohol(request):
    context = {
        'home': False,
        'host': HOST,
        'css_name': create_file_name('alcohol', 'css'),
        'js_name': create_file_name('alcohol', 'js'),
        'title': 'Алкозависимость'
    }
    return render(request, 'alcohol.html', context=context)

def smoking(request):
    context = {
        'home': False,
        'host': HOST,
        'css_name': create_file_name('smoking', 'css'),
        'js_name': create_file_name('smoking', 'js'),
        'title': 'Курение'
    }
    return render(request, 'smoking.html', context=context)

def drugs(request):
    context = {
        'home': False,
        'host': HOST,
        'css_name': create_file_name('drugs', 'css'),
        'js_name': create_file_name('drugs', 'js'),
        'title': 'Наркозависимость'
    }
    return render(request, 'drugs.html', context=context)
