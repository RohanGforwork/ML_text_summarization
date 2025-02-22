from django.urls import path
from .views import SummarizeView, SentimentTranslateView

urlpatterns = [
    path('summarize/', SummarizeView.as_view(), name='summarize'),
    path('sentiment-translate/', SentimentTranslateView.as_view(), name='sentiment-translate'),
]