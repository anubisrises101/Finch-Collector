# main_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm


# Define the home view function
def home(request):
    return render(request, "home.html")


# Define the about view function


def about(request):
    return render(request, "about.html")


def finch_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": finches})


def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
    return render(
        request,
        "finches/detail.html",
        {"finch": finch, "feeding_form": feeding_form, "toys": toys_finch_doesnt_have},
    )


class FinchCreate(CreateView):
    model = Finch
    fields = ["name", "breed", "description", "age"]
    success_url = "/finches/{id}"


class FinchUpdate(UpdateView):
    model = Finch
    fields = ["breed", "description", "age"]


class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches/"


def add_feeding(request, finch_id):
    # request.POST is a QueryDict (dictionary-like object)
    form = FeedingForm(request.POST)
    if form.is_valid():
        # Create a feeding object, but don't save it to the db
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect("finch-detail", finch_id=finch_id)


class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "color"]


class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"

def associate_toy(request, finch_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('finch-detail', finch_id=finch_id)

def remove_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id)
    Toy.objects.get(id=toy_id).remove(toy_id)   
    return redirect('finch-detail', finch_id=finch.id)