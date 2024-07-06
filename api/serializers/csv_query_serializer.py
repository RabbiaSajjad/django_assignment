# csvupload/serializers.py
from rest_framework import serializers

class CSVQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    date = serializers.DateField(required=False)

    min_age = serializers.IntegerField(required=False)
    max_age = serializers.IntegerField(required=False)
    min_date = serializers.DateField(required=False)
    max_date = serializers.DateField(required=False)
    total_greater_than = serializers.IntegerField(required=False)
    total_less_than = serializers.IntegerField(required=False)
