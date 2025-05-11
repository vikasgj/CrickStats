from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('top-run-scorers/', views.top_run_scorers, name='top-run-scorers'),
    path('top-wicket-takers/', views.top_wicket_takers, name='top-wicket-takers'),
    path('highest-scores/', views.highest_individual_scores, name='highest-scores'),
]

