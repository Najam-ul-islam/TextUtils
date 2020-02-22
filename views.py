# This file is created by Najam Ul Islam
from django.http import HttpResponse
# We will use below import to use external files as in templates
from django.shortcuts import render

# Function created to link index name in URLS.py
def index(request):
    # We can use HTML tags as well in HttpResponse()
    # we can pass dictionary in render as well
    # params = {'name':'Najam Ul Islam', 'place': 'Pakistan'}
    # return render(request, 'index.html' ,params)
    return render(request, 'index.html')


# def about(request):
#     return HttpResponse("<h1>About</h1>")
# # File content reading
# def file_content(request):
#     file = "C:\\Najam\\Web developement course\\Django Course\\one.txt"
#     with open(file, 'r', encoding='utf-8') as f:
#         read = f.readlines()
#     return HttpResponse(read)
# # Personal websites navigation bar
# def personal_navigator(request):
#     return HttpResponse("""<h1>Personal Navigator</h1>  
#     <a href='https://google.com'>Google</a><br>
#     <a href='https://youtube.com'>Youtube</a><br>
#     <a href='https://yahoo.com'>Yahoo</a> """)
#===========================================================
# string library contains all punctuations
import string
# string.punctuation  method contains punctuation
punc = string.punctuation
def analyze(request):
    # Get text from user
    djtext = request.POST.get('text', 'default')
    # Check, checkBoxes for feature selection
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    newline_remover = request.POST.get('newlineremover', 'off')
    space_remover = request.POST.get('spaceremover', 'off')
    extra_space_remover = request.POST.get('extraspaceremover', 'off')
    char_count = request.POST.get('charcount', 'off')

    #=======================================================
                     # Remove Punctuations
    #=======================================================
    if remove_punc == "on":
        # Logic to remove punctuation
        analyzed = ""
        for chars in djtext:
            # Here we check that the punctuation is not in given text
            if chars not in punc:
                # then append text characters in analyzed variable
                analyzed = analyzed + chars
        #========================================
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    #=======================================================
                     # UpperCase Text
    #=======================================================
    if full_caps == "on":
        analyzed = ""
        for chars in djtext:
            analyzed = analyzed + chars.upper()
        params = {'purpose':'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    #=======================================================
                    # Newline Remover
    #=======================================================
    if newline_remover == "on":
        analyzed = ""
        for chars in djtext:
            # if newline character exists in text
            if chars != '\n' and chars != '\r':
                analyzed = analyzed + chars
        params = {'purpose':'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    #=======================================================
                    # Space Remover
    #=======================================================
    if space_remover == "on":
        analyzed = ""
        for chars in djtext:
            if "" in chars:
                analyzed = analyzed + chars.strip() 
        params = {'purpose':'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    #=======================================================
                    # Extra Spaces Remover
    #=======================================================
    if extra_space_remover == "on":
        analyzed = ""
        for index,chars in enumerate(djtext):
            # if text has extra spaces then remove  
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + chars
        params = {'purpose':'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    #=======================================================
    #=======================================================
                        # Character Count
    #=======================================================
    if char_count == "on":
        # analyzed = ""
        # # Method-1
        # for char_len in djtext.split():
        #         analyzed = analyzed + str(len(char_len))
        # Method-2
        analyzed = len(djtext)
        params = {'purpose':'Change to Upper Case', 'analyzed_text': analyzed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)
    #=======================================================
    if remove_punc != "on" and full_caps != "on" and newline_remover !="on" and space_remover != "on" and extra_space_remover != "on" and char_count != "on":
        return HttpResponse("Error!!!!!!!\n please select any operation.")
    return render(request, 'analyze.html', params)
#===========================================================
# def removepunc(request):
#     rp = """<h1>Remove Punc</h1><a href='/'> <strong > Back to main page </strong> </a>"""
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyse text
#     return HttpResponse(rp)
# def capatilizefirst(request):
#     cap_first = """<h1>Capatialize First</h1> <button style='width: 10%; margin:10px 10px; padding:20px 10px; border-radius: 20px;>
#             <a href='http://127.0.0.1:8000' name='Remove Punc'> <strong>  Capatial First </strong> </a></button>"""
#     return HttpResponse(cap_first)
# def newlineremove(request):
#     newline_remove = """<h1>New Line Remove</h1> <button style='width: 10%; margin:10px 10px; padding:20px 10px; border-radius: 20px;>
#             <a href='http://127.0.0.1:8000' name='Remove Punc'> <strong> Newline Remove </strong> </a></button>"""
#     return HttpResponse(newline_remove)
# def spaceremove(request):
#     space_remove = """<h1>Space Remove</h1> <button style='width: 10%; margin:10px 10px; padding:20px 10px; border-radius: 20px;>
#             <a href='http://127.0.0.1:8000' name='Remove Punc'> <strong> Space Remove </strong> </a></button>"""
#     return HttpResponse(space_remove)
# def charcount(request):
#     char_count = """<h1>Character Count</h1> <button style='width: 10%; margin:10px 10px; padding:20px 10px; border-radius: 20px;>
#             <a href='http://127.0.0.1:8000' name='Remove Punc'> <strong> Char Count </strong> </a></button>"""
#     return HttpResponse(char_count)
