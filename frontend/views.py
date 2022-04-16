from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'home': True,
        'title': 'Главная'
    }
    return render(request, 'home.html', context=context)

def alcohol(request):
    context = {
        'home': False,
        'title': 'Алкозависимость'
    }
    return render(request, 'alcohol.html', context=context)

def smoking(request):
    context = {
        'home': False,
        'title': 'Курение'
    }
    return render(request, 'smoking.html', context=context)

def drugs(request):
    context = {
        'home': False,
        'title': 'Наркозависимость'
    }
    return render(request, 'drugs.html', context=context)
