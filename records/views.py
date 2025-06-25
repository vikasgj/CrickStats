# records/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Max
from .models import Player, News, Ranking, Team, Record


def home(request):
    return render(request, 'home.html')


def records_home(request):
    top_scorers = (
        Record.objects.values('player__name', 'player__country__name')
        .annotate(total_runs=Sum('runs'))
        .order_by('-total_runs')[:5]
    )
    top_wickets = (
        Record.objects.values('player__name', 'player__country__name')
        .annotate(total_wickets=Sum('wickets'))
        .order_by('-total_wickets')[:5]
    )
    news = News.objects.order_by('-date_posted')[:3]
    return render(request, 'records/home.html', {
        'top_scorers': top_scorers,
        'top_wickets': top_wickets,
        'news': news
    })


def top_run_scorers(request):
    top_runs = (
        Record.objects.values('player__name', 'player__country__name')
        .annotate(total_runs=Sum('runs'))
        .order_by('-total_runs')[:10]
    )
    return render(request, 'records/top_run_scorers.html', {'top_runs': top_runs})


def top_wicket_takers(request):
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


def players_home(request):
    players = Player.objects.select_related('country').all()
    return render(request, 'records/players.html', {'players': players})


def teams_home(request):
    teams = Team.objects.all()
    return render(request, 'records/teams.html', {'teams': teams})


def rankings_home(request):
    rankings = Ranking.objects.select_related('player').order_by('rank')
    return render(request, 'records/rankings.html', {'rankings': rankings})


def news_home(request):
    articles = News.objects.order_by('-date_posted')
    return render(request, 'records/news.html', {'articles': articles})
