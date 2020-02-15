from PIL import Image
import pytesseract
from .models import Post

# Getting the title from DB
title = Post.objects.values('title')
# # Rolling over value from QuerySet
# for i in test:
#     print(i['cover'])

# Mining Starts
for i in title:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Create an image object of PIL library
    image = Image.open(Post.objects.get(title=i['title']).cover)

    # pass image into pytesseract module
    image_to_text = pytesseract.image_to_string(image, lang='eng')

    if len(image_to_text) > 0:
        Post.objects.filter(title=i['title']).update(mined_text=image_to_text)
    else:
        Post.objects.filter(title=i['title']).update(mined_text='No content')
