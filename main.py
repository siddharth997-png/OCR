import pytesseract
import PIL.Image
import cv2

def findAwb(text, first_occ):
    i = first_occ
    awb_start = False
    awb = ""
    while i < len(text):
        if(text[i].isdigit() == False and awb_start == True):
            break

        if(text[i].isdigit() and awb_start == False):
            awb_start = True

        if(awb_start == True):
            awb = awb  + text[i]

        i = i + 1
    return awb


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
    occ = text.find("AWB")
    print("\nFor image ",image)
    
    if occ != -1 : 
        awb = findAwb(text, occ)
        print("AWB : ", awb) 
    else:
        print("OCR unsuccessful")

  