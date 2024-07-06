# api/helpers.py
from django.db.models import Q, Sum, Min, Max, Avg

def build_filters(validated_data):
    filters = Q()

    if 'age' in validated_data:
        filters &= Q(age=validated_data['age'])
    if 'date' in validated_data:
        filters &= Q(date=validated_data['date'])
    if 'name' in validated_data:
        filters &= Q(name__icontains=validated_data['name'])

    return filters

def apply_range_queries(filters, validated_data):
    if 'min_age' in validated_data:
        filters &= Q(age__gte=validated_data['min_age'])
    if 'max_age' in validated_data:
        filters &= Q(age__lte=validated_data['max_age'])
    if 'min_date' in validated_data:
        filters &= Q(date__gte=validated_data['min_date'])
    if 'max_date' in validated_data:
        filters &= Q(date__lte=validated_data['max_date'])

    return filters

def perform_aggregate_searches(queryset, validated_data):
    if 'total_greater_than' in validated_data:
        queryset = queryset.annotate(total=Sum('age')).filter(total__gt=validated_data['total_greater_than'])
    if 'total_less_than' in validated_data:
        queryset = queryset.annotate(total=Sum('age')).filter(total__lt=validated_data['total_less_than'])

    return queryset

def get_aggregate_data(queryset, validated_data):
    if 'total_greater_than' not in validated_data and 'total_less_than' not in validated_data:
        aggregate_data = {
            'max_age': queryset.aggregate(Max('age'))['age__max'],
            'min_age': queryset.aggregate(Min('age'))['age__min'],
            'avg_age': queryset.aggregate(Avg('age'))['age__avg'],
        }
    else:
        aggregate_data = {}

    return aggregate_data
