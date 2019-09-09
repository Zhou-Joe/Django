from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from main.models import Cat, Category
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import NewUserForm


def about(request):
    return render(request=request,
                  template_name="main/about.html")
def breeds(request):
    return render(request=request,
                  template_name="main/breeds.html")


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
    categories = [c.slug for c in Category.objects.all()]
    if single_slug in categories:
        matching_cat = Cat.objects.filter(cat_category__slug=single_slug)
        this_cat_idx=list(categories).index(single_slug)
        return render(request=request,
                      template_name='main/category.html',
                      context={"part_ones": matching_cat.all,
                               "sidebar": Category.objects.all(),
                               "this_cat_idx": this_cat_idx
                               })



    cats = [t.slug for t in Cat.objects.all()]
    if single_slug in cats:
        this_cat = Cat.objects.get(slug=single_slug)
        cat_from_category = Cat.objects.filter(cat_category__category=this_cat.cat_category)
        this_cat_idx = list(cat_from_category).index(this_cat)

        return render(request=request,
                      template_name='main/content.html',
                      context={"cat": this_cat,
                               "sidebar": cat_from_category,
                               "this_cat_idx": this_cat_idx
                      })

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"categories": Category.objects.all()})
