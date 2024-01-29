import easyocr
from PIL import Image

image = Image.open("test adultrants.jpg")
reader = easyocr.Reader(["en"])
text = reader.readtext(image)
test = str(text)

with open("extracted.txt",'r+') as file:
    data =file.write(test)
