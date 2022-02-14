
# Optical Character Recognition 

This project accepts various courier images and extracts the 'AWB' field from the images

## Dependencies

This project is built in python and uses [Tesseract library](https://github.com/tesseract-ocr/tesseract) for OCR. Since Tesseract is not exclusive to python, we have to install pytesseract to make it work with python


## Deployment

To run this project locally, first you need to have python, pip and tesseract installed.

Links : 

- [Python](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html)
  


Then you need to set the tesseract enviroment variable. 
  
    1. Go to Settings->Environment Variables 
    2. Open System Properties
    3. Click on environment Variables
    4. Under Environment Variables, double click on Path
    5. Click on New
    5. Copy the address of the base directory of Tesseract OCR and add the address to the path variable


Then install pillow and pytesseract using the pip package manager from comand line
```cmd
  pip install pillow pytesseract
```

Your local enviroment is set to run the project. Next clone the project 
```
  git clone https://github.com/siddharth997-png/OCR.git
```

Then simply open cmd/bash inside the OCR folder and run the following command : 
```
  python main.py
```



