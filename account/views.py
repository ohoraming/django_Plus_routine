from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from account.forms import SignupForm, SigninForm
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    return render(request, 'account/mainPage.html')


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:login'))
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


@api_view(['GET', 'POST'])
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('account:index') + '?success=1')
    else:
        form = SigninForm()
    return render(request, 'account/login.html', {'form':form})