from django.urls import path
from . import api_views

urlpatterns = [
    path('top-runs/', api_views.api_top_run_scorers),
    path('top-wickets/', api_views.api_top_wicket_takers),
    path('highest-scores/', api_views.api_highest_individual_scores),
]
