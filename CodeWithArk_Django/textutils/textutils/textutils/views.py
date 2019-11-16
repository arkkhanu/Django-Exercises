from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'default')
    analyzed = ""
    punctuator = '''~_-!@#$%^&*()?><:;{}'''
    for char in djtext:
        if char not in punctuator:
            analyzed += char
    params = {'purpose': 'Remove Puncatuators', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
