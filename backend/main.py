from fastapi import FastAPI, File, UploadFile, Body
from fastapi.responses import JSONResponse
from PIL import Image, ImageEnhance
import pytesseract
import io
import spacy

app = FastAPI()

# Load spaCy model globally
nlp = spacy.load("en_core_web_sm")

def preprocess_for_ocr(img: Image.Image) -> Image.Image:
    """
    Applies preprocessing steps to improve OCR accuracy.
    """
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.point(lambda x: 0 if x < 140 else 255, "1")
    img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)
    return img

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    """
    OCR endpoint: receives an image file and returns extracted text.
    """
    contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    img_pre = preprocess_for_ocr(img)
    config = "--psm 6"
    text = pytesseract.image_to_string(img_pre, lang="eng", config=config)
    return JSONResponse({"text": text})

@app.post("/clauses")
async def clauses_endpoint(body: dict = Body(...)):
    """
    Clause detection endpoint: receives JSON with 'text' and returns list of clauses.
    """
    text = body.get("text", "")
    doc = nlp(text)
    clauses = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    return JSONResponse({"clauses": clauses})
