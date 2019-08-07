# I have created this : Akhilesh kuma bhagat
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index2.html')


def removepunc(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check with check box is on
    if removepunc == 'on':
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcount == 'on'):
        analyzed = 0
        for char in djtext:
            analyzed += len(char)

        params = {'purpose': ' total characters are  ', 'analyzed_text': analyzed}
        djtext = analyzed


    # if (spaceremover == 'on'):
    #     analyzed = ""
    #     for index, char in enumerate(djtext):
    #         if not(djtext[index] == '  ' and djtext[index+1] == '  '):
    #             analyzed = analyzed + char
    #     params = {'purpose': 'removed spaces', 'analyzed_text': analyzed}
    #     djtext = analyzed

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and charcount != 'on' and spaceremover != 'on':
        return HttpResponse('Please select at least any one options')

    return render(request, 'analyze.html', params)







































# def capfirst(request):
#     return HttpResponse('captalize first')
#
#
# def newlineremove(request):
#     return HttpResponse('new line remove')
#
#
# def spaceremove(request):
#     return HttpResponse('space remove')
#
#
# def charcount(request):
#     return HttpResponse('char count <a href = "/">Back</a>')


