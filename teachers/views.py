from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def login(request):
    return render(request, 'login.html',)

def account(request):
    return render(request, 'account.html',)

def faculty(request):
    return render(request, 'cafe.html',)
