from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, 'index.html',)


def batafsil(request):
    return render(request, 'batafsil.html',)



def faculty(request):
    return render(request, 'faculty.html',)




@login_required
def account(request):
    return render(request, 'account.html',)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('account')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account')
            return render(request, 'registration/login.html',)
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
