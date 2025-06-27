from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract, io
import spacy
from transformers import pipeline

app = FastAPI()

# 1️⃣ Health‐check
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 2️⃣ OCR endpoint
@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")
    text = pytesseract.image_to_string(image)
    return {"filename": file.filename, "text": text}

# Load NLP once at startup
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")

# 3️⃣ Summarize endpoint
@app.post("/summarize")
async def summarize_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    raw_text = pytesseract.image_to_string(image)
    sections = [sec for sec in raw_text.split("\n\n") if sec.strip()]

    summaries = []
    for sec in sections:
        summary = summarizer(sec, max_length=128, min_length=30, do_sample=False)[0]["summary_text"]
        summaries.append({"original": sec, "summary": summary})

    return {"filename": file.filename, "summaries": summaries}
