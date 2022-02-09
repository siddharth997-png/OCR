import pytesseract
import PIL.Image
import cv2
import re

def findAwb(text):
    i =  text.find("AWB")
    if i == -1:
        return "Not Found"
    awb_start = False
    awb = ""
    while i < len(text):
        if(text[i].isnumeric() == False and awb_start == True):
            break

        if(text[i].isnumeric() and awb_start == False):
            awb_start = True

        if(awb_start == True):
            awb = awb  + text[i]

        i = i + 1
    return awb

def findDimensions(text, attr) :
    i =  text.find(attr)
    if i == -1:
        return "Not Found"
    attr_start = False
    decimal_start = False
    attr = ""
    while(i < len(text)):
        if((attr_start == True and text[i] == ' ') or
           (decimal_start == True and text[i] == '.')) :
            break
        if(attr_start == False and text[i].isdigit()):
            attr_start = True
        if((text[i].isdigit() or text[i] == '.') and attr_start == True):
            attr += text[i]
            if(text[i] == '.'):
                decimal_start = True
        i = i + 1
    return attr


def findProductProperties(text) :
    properties = {}
    properties['AWB'] = findAwb(text)
    height = findDimensions(text, "Height")
    length = findDimensions(text, "Length")
    properties["Height"] = height
    properties["Length"] = length
    return properties



myconfig = r"--psm 6"

images = ["Aramex2_Sample.jpg",
        "Aramex_Sample.jpg","BD_Sample_Image.jpg",
        "Delhivery_Reverse_Sample_Image.jpeg",
        "Delhivery_Sample_Image.jpeg",
        "Delhivery_Surface_10_Kg_Sample_Image.jpeg",
        "Delhivery_Surface_Sample_Image.jpeg",
        "Ecom_Express_Reverse_Sample_Image.jpeg",
        "Ecom_Express_ROS_Reverse_Sample_Image.jpeg","Ecom_Express_Surface_2kg_Sample_Image.jpeg",
        "Ecom_Express_Surface_Sample_Image.jpg",
        "SFX2_Sample.jpg",
        "SFX_Sample.jpg",
        "XB.jpg"
]

for image in images:
    image_path = "all_images/" + image
    text = pytesseract.image_to_string(PIL.Image.open(image_path),config=myconfig)
    
    print("\nFor image ",image)
    if(image == "SFX2_Sample.jpg"):
        print("\nText : \n",text,"\n")
    details = findProductProperties(text)
    print(details)
    
    

  
#   Hex Yellow : #d0bc40, #d0bc40, #dfd12a, #a39b25, #d2ce1f
# white : #f4f4f4
# magick test2.jpg -fill black -fuzz 20% +opaque #d0bc40 op2.jpg