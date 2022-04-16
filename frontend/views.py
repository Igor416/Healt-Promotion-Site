from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'home.html', context=context)

def smoking(request):
    context = {
        'title': 'Курение'
    }
    return render(request, 'smoking.html', context=context)

def alcohol(request):
    context = {
        'title': 'Алкоголь'
    }
    return render(request, 'alcohol.html', context=context)

def drugs(request):
    context = {
        'title': 'Накротики'
    }
    return render(request, 'drugs.html', context=context)
