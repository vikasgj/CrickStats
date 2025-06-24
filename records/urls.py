from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('records/', views.records_home, name='records-home'),
    path('top-run-scorers/', views.top_run_scorers, name='top-run-scorers'),
    path('top-wicket-takers/', views.top_wicket_takers, name='top-wicket-takers'),
    path('highest-scores/', views.highest_individual_scores, name='highest-scores'),
    path('players/', views.players_home, name='players-home'),
    path('teams/', views.teams_home, name='teams-home'),
    path('rankings/', views.rankings_home, name='rankings-home'),
    path('news/', views.news_home, name='news-home'),
]
