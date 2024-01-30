
import easyocr
from PIL import Image
import spacy

def read_image(path):
    image = Image.open(path)
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image)
    return result

def extract_ingredients(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for entity in doc.ents:
        if entity.label_ == "FOOD":
            return True
    return False

result = read_image("test adultrants.jpg")

# Extract ingredients from the text
extracted_ingredients = extract_ingredients(result)

print("Extracted Ingredients:")
print(extracted_ingredients)
