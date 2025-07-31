from django.http import HttpResponse
import requests
from django.shortcuts import render
# from .models import Person


def new(request):
    return render(request,"a.html")

def signup(request):
    if request.POST:
        fname=request.POST['name1']
        lname= request.POST["name2"]
        email= request.POST["email"]
        password = request.POST['pass']
        print(fname,lname,email,password)

    return render (request,"signup.html")