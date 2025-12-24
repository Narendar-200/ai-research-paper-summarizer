import torch#This uses AI to summarize text
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):
    text = text[:2000]  # limit size

    summary = summarizer(
        text,
        max_length=150,
        min_length=60,
        do_sample=False
    )

    return summary[0]["summary_text"]
