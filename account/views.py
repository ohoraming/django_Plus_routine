from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from account.forms import UserForm

# Create your views here.

def index(request):
    return render(request, 'account/mainPage.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})