from django.shortcuts import render
from .models import English, Slick, Phonetics, Сurriculum


def index(request):
    lessons = English.objects.filter().order_by("id")
    slicks = Slick.objects.get(id=1)
    phonetics = Phonetics.objects.filter().order_by("id")
    curriculum = Сurriculum.objects.get(id=1)
    return render(request, "english/index.html", {'lessons': lessons, 'slicks': slicks, 'phonetics': phonetics, 'curriculum': curriculum})


def about(request):
    return render(request, "english/about.html")
