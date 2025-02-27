from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples = [
        {'Name' : 'Pratik jagtap', 'Age' : 22},
        {'Name' : 'Pratiksha Jagtap', 'Age' : 18},
        {'Name' : 'Komal Kolate', 'Age' : 22},
        {'Name' : 'Anand Shinde', 'Age' : 15},
        {'Name' : 'Rohit Sharma', 'Age' : 45},
        {'Name' : 'Schin Kolhe', 'Age' : 22},
        
        
    ]

    return render(request , "index.html", context={'peoples' : peoples})


def about(request):
    return render(request , "about.html")


def base(request):
    return render(request , "base.html")
