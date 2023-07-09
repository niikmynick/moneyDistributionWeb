from django.http import JsonResponse
from django.shortcuts import render
from django.template import Template, Context


def index(request):
    return render(request, '../templates/index.html', {})


def about(request):
    return render(request, '../templates/about.html', {})


def account(request):
    return render(request, '../templates/account.html', {})


def application(request):
    return render(request, '../templates/application.html', {})


    return form_html(creditors, ratio, creditors_get, bank_payments, total_fees)


def application_result(request):
    if request.method == 'POST':
        response = {'html': html_result(request)}
        return JsonResponse(response)
