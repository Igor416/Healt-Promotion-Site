from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('smoking/', views.smoking, name = 'smoking'),
    path('alcohol/', views.alcohol, name = 'alcohol'),
    path('drugs/', views.drugs, name = 'drugs')
]
