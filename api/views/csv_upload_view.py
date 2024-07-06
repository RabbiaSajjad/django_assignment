import csv
import logging
from datetime import datetime
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from ..serializers.csv_upload_serializer import CSVFileUploadSerializer
from ..models import DataRecord

logger = logging.getLogger('csvupload')

class CSVFileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = CSVFileUploadSerializer(data=request.data)
        if serializer.is_valid():
            csv_file = serializer.validated_data['csv_file']
            file_path = f'/tmp/{csv_file.name}'
            with open(file_path, 'wb+') as temp_file:
                for chunk in csv_file.chunks():
                    temp_file.write(chunk)

            self.load_csv_data(file_path)

            return Response({'message': 'File uploaded and processed successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def load_csv_data(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    try:
                        age = int(row['age'])
                    except ValueError:
                        age = 0

                    try:
                        date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                    except ValueError:
                        date = ""

                    record, created = DataRecord.objects.get_or_create(
                        name=row['name'],
                        age=age,
                        date=date,
                    )

                    if created:
                        logger.debug(f'Record created: {record}')
                    else:
                        logger.warning(f'Record already exists: {record}')

                except IntegrityError:
                    logger.error(f'Integrity error for record: {row}')
