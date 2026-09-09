from django.shortcuts import render

def BaseView(request):
    return render(request,"landing.html")

def CalendarView(request):
    return render(request,"calendar.html")

def CalendarViewMonth(request):
    return render(request,"calendar_month.html")

def ChampionshipsView(request):
    return render(request,"championships.html")

def ChampionshipDetailView(request, slug):
    return render(request, "championship_detail.html", {"slug": slug})
