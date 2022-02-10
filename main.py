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
    awb = findAwb(text)
    if(awb == "Not Found") :
        awb = findDimensions(text, "Barcode")
    height = findDimensions(text, "Height")
    if(height == "Not Found") :
        heigh = findDimensions(text, "H")
    length = findDimensions(text, "Length")
    if(length == "Not Found") :
        length = findDimensions(text, "L")
    properties['AWB'] = awb
    properties["Height"] = height
    properties["Length"] = length
    return properties



myconfig = r"--psm 6"

converted_images = ["op1.jpg",
        "op2.jpg",
        "op3.jpg",
        "op4.jpg",
        "op5.jpg",
        "op6.jpg",
        "op7.jpg",
        "op8.jpg",
        "op9.jpg",
        "op10.jpg",
]

og_images = ["Aramex_Sample.jpg",
        "Aramex2_Sample.jpg",
        "BD_Sample_Image.jpg",
        "Delhivery_Reverse_Sample_Image.jpeg",
        "Delhivery_Sample_Image.jpeg",
        # "Delhivery_Surface_10_Kg_Sample_Image.jpeg",
        "Delhivery_Surface_Sample_Image.jpeg",
        "Ecom_Express_Reverse_Sample_Image.jpeg",
        "Ecom_Express_ROS_Reverse_Sample_Image.jpeg",
        "Ecom_Express_Surface_2kg_Sample_Image.jpeg",
        "XB.jpg"
]

for i in range(0,10):
    converted_image_path = "converted/" + converted_images[i]
    real_image_path = "all_images/" + og_images[i] 
    print("\nFor image ",og_images[i])
    text = pytesseract.image_to_string(PIL.Image.open(converted_image_path),config=myconfig)
    print("Details from Converted Image : ")
    print(findProductProperties(text))
    text = pytesseract.image_to_string(PIL.Image.open(real_image_path),config=myconfig)
    print("Details from Real Image : ")
    print(findProductProperties(text))
    

  
#   Hex Yellow : #d0bc40, #d0bc40, #dfd12a, #a39b25, #d2ce1f
# white : #f4f4f4
# magick test2.jpg -fill black -fuzz 20% +opaque #d0bc40 op2.jpg