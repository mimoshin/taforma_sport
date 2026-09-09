from django.shortcuts import render
from django.http import Http404

CHAMPIONSHIP_EVENTS = {
    "garrocha": "Salto con Garrocha",
    "100mv": "100 m Vallas",
    "bala": "Lanzamiento Bala",
    "jabalina": "Lanzamiento Jabalina",
    "salto-largo": "Salto Largo",
    "salto-alto": "Salto Alto",
    "100mp": "100 m Planos",
    "martillo": "Lanzamiento Martillo",
    "2000m": "2.000 m Planos",
    "300mv": "300 m Vallas",
}

def BaseView(request):
    return render(request,"landing.html")

def CalendarView(request):
    return render(request,"calendar.html")

def CalendarViewMonth(request):
    return render(request,"calendar_month.html")

def ChampionshipsView(request):
    return render(request,"championships.html")

def ChampionshipDetailView(request, slug):
    return render(request, "championship_results.html", {"slug": slug, "active_tab": "resultados"})

def ChampionshipScheduleView(request, slug):
    return render(request, "championship_schedule.html", {"slug": slug, "active_tab": "horario"})

def ChampionshipEventResultsView(request, slug, event_slug):
    if event_slug not in CHAMPIONSHIP_EVENTS:
        raise Http404("Prueba no encontrada")

    return render(request, "championship_event_results.html", {
        "slug": slug,
        "active_tab": "resultados",
        "active_event": event_slug,
        "event_name": CHAMPIONSHIP_EVENTS[event_slug],
    })

def RankingView(request):
    return render(request, "ranking.html")

def ChampionshipScoresView(request, slug):
    return render(request, "championship_scores.html", {"slug": slug, "active_tab": "puntajes"})

def LoginPageView(request):
    return render(request, "login.html")

def RegisterPageView(request):
    return render(request, "register.html")
