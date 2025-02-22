from django.urls import path
from .views import LoginView, SummarizeView, SentimentView, TranslateView, UploadDatasetView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('summarize/', SummarizeView.as_view(), name='summarize'),
    path('sentiment/', SentimentView.as_view(), name='sentiment'),
    path('translate/', TranslateView.as_view(), name='translate'),
    path('upload-dataset/', UploadDatasetView.as_view(), name='upload-dataset'),
]