from django.shortcuts import render


def index(request):
    return render(request, '../templates/index.html', {})


def about(request):
    return render(request, '../templates/about.html', {})


def account(request):
    return render(request, '../templates/account.html', {})


def application(request):
    return render(request, '../templates/application.html', {})
