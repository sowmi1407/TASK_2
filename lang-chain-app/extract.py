import pytesseract
from PIL import Image

def extract_text_from_images(image_files):
    result = []
    for image_file in image_files:
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img)
        result.append(text.strip())
    return result 