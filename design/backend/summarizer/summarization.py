import torch
from transformers import LongT5ForConditionalGeneration, AutoTokenizer

# Load the model and tokenizer globally to avoid reloading on each request
model = LongT5ForConditionalGeneration.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps")
tokenizer = AutoTokenizer.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps")

def summarize_text(text):
    """
    Summarizes the input text using the LongT5 model.
    :param text: Input text to summarize.
    :return: Summarized text.
    """
    # Preprocess and tokenize the text
    input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1000, truncation=True)

    # Generate summary using the LongT5 model
    summary_ids = model.generate(input_ids, max_length=512, num_beams=1, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary