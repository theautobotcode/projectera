from django.shortcuts import render

# Create your views here.
def loginpage(r):
    return render(r, "login.html")