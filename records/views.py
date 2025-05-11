from django.shortcuts import render

from . import models
from .models import Record
from django.db.models import Sum, Max

from django.shortcuts import render

def home_view(request):
    return render(request, 'records/home.html')

def top_run_scorers(request):
    top_runs = (
        Record.objects.values('player__name', 'player__country__name')
        .annotate(total_runs=Sum('runs'))
        .order_by('-total_runs')[:10]
    )
    return render(request, 'records/top_run_scorers.html', {'top_runs': top_runs})

def top_wicket_takers(request):
    print("In top_wicket_takers view function")
    top_wickets = (
        Record.objects.values('player__name', 'player__country__name')
        .annotate(total_wickets=Sum('wickets'))
        .order_by('-total_wickets')[:10]
    )
    return render(request, 'records/top_wicket_takers.html', {'top_wickets': top_wickets})

def highest_individual_scores(request):
    top_scores = (
        Record.objects.select_related('player', 'match')
        .order_by('-runs')[:10]
    )
    return render(request, 'records/highest_individual_scores.html', {'top_scores': top_scores})
