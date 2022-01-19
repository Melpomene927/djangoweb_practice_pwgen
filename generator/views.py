import re
from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.
def password(request):
    _chars = [ chr(i) for i in range(97, 123)]
    print(request.GET)

    _length = request.GET.get('input-length')
    _length = _length if len(_length) > 0 else request.GET.get('length')

    _num = request.GET.get('number')
    if _num != None:
        _chars += [ chr(i) for i in range(48, 58) ]

    _ucase = request.GET.get('uppercase')
    if _ucase != None:
        _chars += [ chr(i) for i in range(65, 91) ]

    _special = request.GET.get('special')
    if _special != None:
        _chars += list('~!@#$%^&*()_+=-/\[]{}<>,.;:')

    print(_chars)
    _pw = "".join([ _chars[randint(0, len(_chars) -1)] for j in range(eval(_length))])
    return render(request, "password.html", {"password": _pw})

def index(request):
    # _msg = 'Hello Django!!!'
    # print(_msg)
    # return HttpResponse(_msg)
    return render(request, "index.html")

def test(request):
    _html = "<h1>Hello!!!!</h1>"
    return HttpResponse(_html)