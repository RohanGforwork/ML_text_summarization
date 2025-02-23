!pip install googletrans==4.0.0-rc1 better_profanity nltk
!pip install wordfilter

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googletrans import Translator
from scipy.special import softmax

# Load model and tokenizer globally to avoid reloading on each call
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment").to(device)
model.eval()
translator = Translator()

LABELS = ["Negative", "Neutral", "Positive"]

def detect_language(text):
    """
    Detects the language of the input text.
    :param text: Input text.
    :return: Detected language and confidence score.
    """
    detected = translator.detect(text)
    return detected.lang if detected else "unknown", round(detected.confidence, 2) if detected and detected.confidence else 1.0

def translate_text(text, target_lang="en"):
    """
    Translates the text to English if it's not already in English.
    :param text: Input text.
    :param target_lang: Target language (default: English).
    :return: Translated text.
    """
    detected_lang, _ = detect_language(text)
    return translator.translate(text, dest=target_lang).text if detected_lang != target_lang else text

def analyze_sentiment(text):
    """
    Analyzes sentiment of the translated text.
    :param text: English text for sentiment analysis.
    :return: Sentiment label, confidence, and topic-based inference.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        scores = softmax(outputs.logits.cpu().numpy()[0])

    sentiment = LABELS[scores.argmax()]
    confidence = round(scores.max(), 2)

    # Extract topic from the text
    topic = text.split('.')[0] if '.' in text else text[:50]

    # Generate inference with topic reference
    if sentiment == "Positive":
        inference = f"The discussion on '{topic}' is optimistic, suggesting support and approval."
    elif sentiment == "Negative":
        inference = f"The discussion on '{topic}' is critical, indicating concerns or disapproval."
    else:
        inference = f"The sentiment around '{topic}' is mixed, with both positive and negative perspectives present."

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "inference": inference,
        "scores": {LABELS[i]: round(float(scores[i]), 2) for i in range(len(scores))}
    }

def process_text(text):
    """
    Full pipeline: Detect language, translate (if needed), and analyze sentiment.
    :param text: User input text.
    :return: Structured output containing all analysis results.
    """
    detected_lang, lang_confidence = detect_language(text)
    translated_text = translate_text(text)
    sentiment_result = analyze_sentiment(translated_text)

    return {
        "Detected Language": detected_lang,
        "Language Confidence": lang_confidence,
        "Translated Text": translated_text,
        "Sentiment": sentiment_result["sentiment"],
        "Sentiment Confidence": sentiment_result["confidence"],
        "Inference": sentiment_result["inference"]
    }