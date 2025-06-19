import pytesseract
from pathlib import Path
from PIL import Image, ImageFilter
from PIL import ImageEnhance


img_dir = Path('../') 

first_img_name = 'download.png'  
second_img_name = 'form33-fb76abc740b79e9ec50d16d19ac8537748e4d9da09f923d4bc35f9d9e01b2fe1.jpg' 
third_img_name = 'MultiCol1OL.png'   


def process_first_image(img_path):
    img = Image.open(img_path)
    img = Image.open(img_path).convert('L')
    img = img.resize((img.width * 2, img.height * 2)) 
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))  
    return img

def process_second_image(img_path):
    img = Image.open(img_path)
    img = img.convert('L')  
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0) 
    threshold = 150
    img = img.point(lambda x: 0 if x < threshold else 255, '1')
    return img 

def process_third_image(img_path):
    img = Image.open(img_path)
    return img

first_img_path = img_dir / first_img_name
second_img_path = img_dir / second_img_name
third_img_path = img_dir / third_img_name

img1 = process_first_image(first_img_path)
img2 = process_second_image(second_img_path)
img3 = process_third_image(third_img_path)

config_img1 = '--oem 3 --psm 3' 
config_img2 = '--oem 3 --psm 4' 
config_img3 = '--oem 3 --psm 1'  

text1 = pytesseract.image_to_string(img1, config=config_img1)
text2 = pytesseract.image_to_string(img2, config=config_img2)
text3 = pytesseract.image_to_string(img3, config=config_img3)

#print(f'Extracted text from {first_img_name}:\n{text1}\n---------------\n')
print(f'Extracted text from {second_img_name}:\n{text2}\n---------------\n')
#print(f'Extracted text from {third_img_name}:\n{text3}\n---------------\n')
