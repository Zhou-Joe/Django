from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from main.models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import NewUserForm


def welcome(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})
    form = NewUserForm
    return render(request=request,
                  template_name='main/register.html',
                  context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged in with password as {password}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        return render(request=request,
                      template_name='main/category.html',
                      context={"part_ones": matching_series.all})

    series = [s.tutorial_series for s in TutorialSeries.objects.all()]
    if single_slug in series:
        matching_tutorial = Tutorial.objects.filter(tutorial_series__tutorial_series=single_slug)
        return render(request=request,
                      template_name='main/series.html',
                      context={"part_ones": matching_tutorial.all})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tut_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series)
        this_tut_idx = list(tut_from_series).index(this_tutorial)

        return render(request=request,
                      template_name='main/content.html',
                      context={"tutorial": this_tutorial,
                               "sidebar": tut_from_series,
                               "this_tut_idx": this_tut_idx})

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"categories": TutorialCategory.objects.all})
