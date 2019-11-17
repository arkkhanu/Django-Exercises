from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuator = '''~_-!@#$%^&*()?><:;{}'''
        for char in djtext:
            if char not in punctuator:
                analyzed += char
        params = {'purpose': 'Remove Puncatuators', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == 'on':
        analye = ""
        for char in djtext:
            analye += char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analye}
        return render(request, 'analyze.html', params)
    elif newlineremover == 'on':
        analyze = ""
        for char in djtext:
            if char != '\n':
                analyze += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == 'on':
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyze += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyze}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')
