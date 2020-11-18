# I myself have created this file - Sanjeev Kumar

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, Django")
    return render(request, 'index.html')

def about(request):
    # my_file = open("about_me.txt")
    # string = my_file.read()
    # my_file.close()
    # return HttpResponse(string)
    return HttpResponse("About Sanjeev <a href = '/'>back</a>")

def analyze(request):
    # Get the text
    django_user_text = request.POST.get('user_text', 'default_text')
    # Analyze the text
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    purpose = ""
    analyzed_text = ""
    if removepunc == 'on':
        puncutations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in django_user_text:
            if char not in puncutations:
                analyzed = analyzed + char
        # params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose += 'Remove Punctuations'
        analyzed_text += analyzed

    if capitalize == 'on':
        analyzed = django_user_text.upper()
        # params = {'purpose': 'CONVERT TO UPPER CASE', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose += ' | CONVERT TO UPPER CASE '
        analyzed_text = analyzed

    if newlineremove == 'on':
        analyzed = ""
        for char in django_user_text:
            if char is not '\n' and char is not '\r':
                analyzed += char
        # params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose += '| New Line Remove '
        analyzed_text = analyzed

    if extraspaceremove == 'on':
        analyzed = ""
        for index, char in enumerate(django_user_text):
            if not(django_user_text[index] == " " and django_user_text[index + 1] == " "):
                analyzed += char
        # params = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        purpose += '| Extra Space Remove '
        analyzed_text = analyzed

    if charcount == 'on':
        count = len(django_user_text)
        # params = {'purpose': 'Character Count', 'analyzed_text': count}
        # return render(request, 'analyze.html', params)
        purpose += '| Character Count '
        analyzed_text += '<br>Character count is ' + str(count)

    if purpose == "":
        return HttpResponse("Error")
    else:
        return render(request, 'analyze.html', {'purpose': purpose, 'analyzed_text': analyzed_text})

# def removepunc(request):
#     # Get the text
#     django_user_text = request.GET.get('user_text', 'default_text')
#     print(django_user_text)
#     # Analyze the text
#     return HttpResponse("remove punc <a href = '/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first <a href = '/'>back</a>")
#
# def newlineremove(request):
#     return HttpResponse("new line remove <a href = '/'>back</a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href = '/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character count <a href = '/'>back</a>")
