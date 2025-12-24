import json
import os
from pdf_reader import read_pdf
from summarizer import summarize_text

# Project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct absolute paths
pdf_path = os.path.join(BASE_DIR, "input_pdfs", "sample.pdf")
output_path = os.path.join(BASE_DIR, "output", "summary.json")

print("Looking for PDF at:", pdf_path)
print("File exists?", os.path.exists(pdf_path))

print("Reading PDF...")
text = read_pdf(pdf_path)

print("Summarizing...")
summary = summarize_text(text)

result = {
    "file": "sample.pdf",
    "summary": summary
}

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("Done! Summary saved successfully.")
