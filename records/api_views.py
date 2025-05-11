from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Max
from .models import Record
from .serializers import RecordSerializer
from datetime import datetime
from django.db.models import Sum, Q

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Sum, Q
from collections import OrderedDict

@api_view(['GET'])
def api_top_run_scorers(request):
    format = request.GET.get('format')
    year = request.GET.get('year')
    team = request.GET.get('team')
    sort = request.GET.get('sort', '-total_runs')  # default: descending

    filters = Q()
    if format:
        filters &= Q(match__format=format)
    if year:
        filters &= Q(match__date__year=year)
    if team:
        filters &= Q(player__country__name__icontains=team)

    qs = (
        Record.objects.filter(filters)
        .values('player__name', 'player__country__name')
        .annotate(total_runs=Sum('runs'))
        .order_by(sort)
    )

    # Manual pagination
    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(qs, request)
    return paginator.get_paginated_response(page)


@api_view(['GET'])
def api_top_wicket_takers(request):
    format = request.GET.get('format')
    year = request.GET.get('year')
    team = request.GET.get('team')
    sort = request.GET.get('sort', '-total_wickets')  # default descending

    filters = Q()
    if format:
        filters &= Q(match__format=format)
    if year:
        filters &= Q(match__date__year=year)
    if team:
        filters &= Q(player__country__name__icontains=team)

    qs = (
        Record.objects.filter(filters)
        .values('player__name', 'player__country__name')
        .annotate(total_wickets=Sum('wickets'))
        .order_by(sort)
    )

    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(qs, request)
    return paginator.get_paginated_response(page)


@api_view(['GET'])
def api_highest_individual_scores(request):
    format = request.GET.get('format')
    year = request.GET.get('year')
    team = request.GET.get('team')
    sort = request.GET.get('sort', '-runs')  # default: highest score first

    filters = Q()
    if format:
        filters &= Q(match__format=format)
    if year:
        filters &= Q(match__date__year=year)
    if team:
        filters &= Q(player__country__name__icontains=team)

    qs = (
        Record.objects.select_related('player', 'match')
        .filter(filters)
        .order_by(sort)
    )

    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(qs, request)
    serializer = RecordSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

