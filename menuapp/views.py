from django.shortcuts import render
from .models import MenuItem
from django.template import RequestContext


def menu_view(request, menu_name):
    return render(request, 'menu.html')


def about_view(request, menu_name='main_menu'):
    return render(request, 'about.html')
