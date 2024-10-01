# main_app/views.py

from django.shortcuts import render
from .models import Finch

# Define the home view function
def home(request):
    return render(request, "home.html")


# Define the about view function


def about(request):
    return render(request, "about.html")


def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})