from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html',{'hithere':'hero'})

def aj(request):
    return HttpResponse('Hello Hero ;)')

def count(request):

    fulltext = request.GET['text']
    wordlist=fulltext.split()

    worddict=dict()

    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1





    return render(request,'count.html',{'atext':fulltext,'count':len(wordlist),'words':worddict.items()})


def about(request):
    return render(request,'about.html')