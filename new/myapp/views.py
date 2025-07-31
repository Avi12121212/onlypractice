from django.shortcuts import render,HttpResponse
from .models import Book

# Create your views here.
def new(request):
    # book= Book(name="javabook",subject="java",price="550")
    # book.save()

    return HttpResponse("hrlloindia")

def book(request):
    if request.GET:
        name= request.GET["bname"]
        subject= request.GET['subject']
        price=str(request.GET['price'])
        print(name , subject , price)

        book= Book(name=name,subject=subject,price=price)
        book.save()
    return render(request,"book.html")