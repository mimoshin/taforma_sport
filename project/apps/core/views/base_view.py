from django.shortcuts import render

def BaseView(request):
    return render(request,"principal.html")
