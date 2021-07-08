import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import User, Seminar, Review, Category, comments, Partis

 # Create your views here.


def index(request):
    return render(request, "index.html", {
        "seminar": Seminar.objects.filter(is_ended=False),
        "category": Category.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

class seminarform(forms.Form):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, initial=None)


def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["titel"]
            des = request.POST["description"]
            start = request.POST["start"]
            end = request.POST["end"]
            date = request.POST["date"]
            img = request.POST["url"]
            cat = request.POST["cat"]
            Seminar.objects.create(user = request.user, seminar_titel = title, seminar_description = des, start_time = start, end_time = end, url_image = img, date= date, category = cat, is_leader = True)
            return HttpResponseRedirect(reverse('index'))
    return render(request, "createseminar.html", {
        "category": Category.objects.all()
    })

@csrf_exempt
def detail(request, seminar_id):
    s = Seminar.objects.get(id=seminar_id)
    if s.user == request.user:
        leader = True
    else:
        leader = False
    if request.method == "PUT":
        value = json.loads(request.body)
        if value.get("rating") is not None:
            s.seminar_rating = value["rating"]
            s.counter += 1
        s.save()

    if request.method == "POST":
        comment = request.POST["comment"]
        if comment != "":
            comments.objects.create(user = request.user, comment = comment, seminar = s)

    return render(request, "detail.html", {
        "seminar": s,
        "comment": comments.objects.filter(seminar = s),
        "part": Partis.objects.filter(part=request.user, seminar=s).count(),
        "leader": leader
    })

def part(request, id):
    if request.user.is_authenticated:
        s = Seminar.objects.get(id=id)
        button = "participate" if Partis.objects.filter(part=request.user, seminar=s).count() == 0 else "check out from course"
        if request.method == "POST":
            if request.POST["button"] == "participate":
                button = "check out from course"
                Partis.objects.create(part=request.user, seminar=s)
            else:
                button = "participate"
                Partis.objects.get(part=request.user, seminar=s).delete()
    
        return render(request, "part.html", {
        "seminar": s,
        "button": button
    })

def close(request, id):
    s = Seminar.objects.get(id=id)
    s.is_ended = True
    s.save()
    return render(request, "index.html", {
        "seminar": Seminar.objects.filter(is_ended=False)
    })

def mycourses(request):
    s = Seminar.objects.filter(user = request.user)
    p = Partis.objects.filter(part = request.user)
    return render(request, "mycourses.html", {
        "seminar": p,
    })
