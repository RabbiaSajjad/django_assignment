# api/urls.py
from django.urls import path
from .views import CSVFileUploadView

urlpatterns = [
    path('upload-csv/', CSVFileUploadView.as_view(), name='upload_csv'),
]
