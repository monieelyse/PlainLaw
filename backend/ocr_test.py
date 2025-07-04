from PIL import Image
import pytesseract
import os

path = os.path.join("samples", "contract-page1.png")
print("Exists:", os.path.exists(path))

img = Image.open(path)
print("Image size:", img.size, "Mode:", img.mode)

# pop open the image so you can see if it’s legible
img.show()

text = pytesseract.image_to_string(img, lang="eng")
print("Raw OCR length:", len(text))
print("Raw preview:", repr(text[:200]))
