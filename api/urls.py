# api/urls.py
from django.urls import path
from .views import CSVFileUploadView, CSVQueryView

urlpatterns = [
    path('upload-csv/', CSVFileUploadView.as_view(), name='upload_csv'),
    path('query-csv/', CSVQueryView.as_view(), name='query_csv'),
]
