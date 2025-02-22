from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import firebase_admin
from firebase_admin import auth
from .models import User
from transformers import pipeline

class LoginView(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            email = decoded_token['email']
            user, created = User.objects.get_or_create(uid=uid, email=email)
            return Response({"message": "Login successful", "user": email}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class SummarizeView(APIView):
    def post(self, request):
        text = request.data.get('text')
        if len(text) > 1000:
            return Response({"error": "Text exceeds 1000 words"}, status=status.HTTP_400_BAD_REQUEST)
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return Response({"summary": summary[0]['summary_text']}, status=status.HTTP_200_OK)
    
    


sentiment_analyzer = pipeline("sentiment-analysis")

class SentimentView(APIView):
    def post(self, request):
        text = request.data.get('text')
        sentiment = sentiment_analyzer(text)
        return Response({"sentiment": sentiment[0]}, status=status.HTTP_200_OK)
    

translator = pipeline("translation_en_to_fr")

class TranslateView(APIView):
    def post(self, request):
        text = request.data.get('text')
        translation = translator(text)
        return Response({"translation": translation[0]['translation_text']}, status=status.HTTP_200_OK)
    
from .models import UserDataset

class UploadDatasetView(APIView):
    def post(self, request):
        user = request.user
        dataset = request.FILES.get('dataset')
        UserDataset.objects.create(user=user, dataset=dataset)
        return Response({"message": "Dataset uploaded successfully"}, status=status.HTTP_200_OK)