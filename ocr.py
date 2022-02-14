import pytesseract
import PIL.Image
import sys

myconfig = r"--psm 6"

n = len(sys.argv)

image_path = sys.argv[1]
text = pytesseract.image_to_string(PIL.Image.open(image_path),config=myconfig)

print(text)

