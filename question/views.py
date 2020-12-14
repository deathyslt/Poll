from django.shortcuts import render
from django.http.response import HttpResponseNotAllowed
from .froms import LoginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Question


def home(request):
    if request.method == "GET":

        questions = Question.objects.all()
        questions = questions[-5]
        context = {'questions': questions}

        return render(request, 'home.html', context=context)
    else:
        return HttpResponseNotAllowed('not allowed')


def signup_account(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})

    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return redirect('signup')
    else:
        return HttpResponseNotAllowed('not allowed')


def login_account(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': LoginForm()})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
        return redirect('/')




