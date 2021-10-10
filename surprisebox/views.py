from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView


def index(request):
    return render(request, 'surprisebox/index.html', {})


def delivery(request):
    return render(request, 'surprisebox/dostavka-i-oplata.html', {})


def whose_gift(request):
    return render(request, 'surprisebox/komu-podarok.html', {})


def female_gift(request):
    return render(request, 'surprisebox/podarok-devushke.html', {})


def male_gift(request):
    return render(request, 'surprisebox/podarok-parnju.html', {})


def about(request):
    return render(request, 'surprisebox/o-nas.html', {})
