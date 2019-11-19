from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuator = '''~_-!@#$%^&*()?><:;{}'''
        for char in djtext:
            if char not in punctuator:
                analyzed += char
        params = {'purpose': 'Remove Puncatuators', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if fullcaps == 'on':
        analye = ""
        for char in djtext:
            analye += char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analye}
        # return render(request, 'analyze.html', params)
        djtext = analye
    if newlineremover == 'on':
        analyze = ""
        for char in djtext:
            if char != '\n':
                analyze += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', params)
        djtext = analyze
    if extraspaceremover == 'on':
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '):
                analyze += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyze}
        # return render(request, 'analyze.html', params)
        djtext = analyze
    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on':
        return HttpResponse('Error')
    return render(request, 'analyze.html', params)
