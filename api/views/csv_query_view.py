# csvupload/views.py
import logging
from django.db.models import Q, Sum, Min, Max, Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.csv_query_serializer import CSVQuerySerializer
from ..models import DataRecord
from ..helpers import build_filters, apply_range_queries, perform_aggregate_searches, get_aggregate_data

logger = logging.getLogger('csvupload')

class CSVQueryView(APIView):

    def get(self, request, format=None):
        serializer = CSVQuerySerializer(data=request.query_params)
        if serializer.is_valid():
            queryset = DataRecord.objects.all()
            filters = build_filters(serializer.validated_data)
            filters = apply_range_queries(filters, serializer.validated_data)
            queryset = queryset.filter(filters)
            queryset = perform_aggregate_searches(queryset, serializer.validated_data)
            aggregate_data = get_aggregate_data(queryset, serializer.validated_data)

            result = list(queryset.values())
            response_data = {
                'results': result,
                'aggregates': aggregate_data,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
