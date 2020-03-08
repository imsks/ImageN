# from PIL import Image
# import pytesseract
# from .models import Post
#
#
# # Getting the title from DB
# title = Post.objects.values('title')
#
#
# # Mining Starts
# # Sets the path for tesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# # Loops over the column 'title'
# for i in title:
#     # Get status of mining of the data and store in 'isMined'
#     isMined = Post.objects.get(title=i['title']).mined_text
#
#     # Checks if image is mined and stored in database or not => If not then mining starts
#     if isMined == 'Not mined':
#         # Create an image object of PIL library
#         image = Image.open(Post.objects.get(title=i['title']).cover)
#
#         # Pass image into pytesseract module
#         image_to_text = pytesseract.image_to_string(image, lang='eng')
#
#         # Checks if the data is there or not
#         if len(image_to_text) > 0:
#             Post.objects.filter(title=i['title']).update(mined_text=image_to_text)
#         else:
#             Post.objects.filter(title=i['title']).update(mined_text='No content')
