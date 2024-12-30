from django.shortcuts import render

def loginpage(r):
    return render(r, "login.html")