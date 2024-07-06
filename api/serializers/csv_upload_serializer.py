#csv_upload_serializer.py
from rest_framework import serializers

class CSVFileUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
