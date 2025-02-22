from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .sentiment_translator import process_text
from .summarization import summarize_text

class SummarizeView(APIView):
    def post(self, request):
        """
        Handles POST requests for text summarization.
        """
        text = request.data.get('text')
        if not text:
            return Response({"error": "Text is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call the summarization function
            summary = summarize_text(text)
            return Response({"summary": summary}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SentimentTranslateView(APIView):
    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({"error": "Text is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = process_text(text)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)