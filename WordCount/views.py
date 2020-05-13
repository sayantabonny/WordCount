from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
def basic(request):
    #return "Hello"
    return HttpResponse('Hello')


def basic1(request):
    #return "Hello"
    return HttpResponse('<h1> Hello <h1/>')

def index(request):
    #return "Hello"
    return render(request,"Index.html")

def index1(request):
    #return "Hello"
    return render(request,"Index1.html",{'Key1':'Sayanta','Key2':'Mukherjee'})

def Input(request):
    #return "Hello"
    return render(request,"Input.html")

def Count(request):
    #return "Hello"
    Count_dic=Counter(request.GET['Text'].split())
    return render(request,"Count.html",{'List_Tup':Count_dic.items()})



