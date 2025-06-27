import re
import spacy
from transformers import pipeline

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

# Initialize summarization pipeline
summarizer = pipeline("summarization")

def split_into_sections(text: str) -> list[str]:
    """
    Naively split by two or more newlines to get logical sections.
    """
    # You can refine this with spaCy heading detection later.
    sections = re.split(r'\n{2,}', text.strip())
    return [s for s in sections if s.strip()]

def summarize_section(section: str, max_length=128) -> str:
    """
    Use Hugging Face summarizer to condense a section.
    """
    # The pipeline expects up to ~1024 tokens; you may chunk if larger.
    result = summarizer(section, max_length=max_length, min_length=30, do_sample=False)
    return result[0]["summary_text"]
