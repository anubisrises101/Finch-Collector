# main_app/views.py

from django.shortcuts import render


# Define the home view function
def home(request):
    return render(request, "home.html")


# Define the about view function


def about(request):
    return render(request, "about.html")


class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


# Create a list of Finch instances
finches = [
    Finch("Lolo", "House Finch", "Kinda nice.", 3),
    Finch("Sachi", "Rose Finch", "reddish pink.", 0),
    Finch("Fancy", "Purple Finch", "Happy fluff ball.", 4),
    Finch("Bonk", "Eurasian Bullfinch", "loud.", 6),
]


def finch_index(request):
    # Render the finches/index.html template with the finches data
    return render(request, "finches/index.html", {"finches": finches})
