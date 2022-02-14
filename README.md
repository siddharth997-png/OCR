
# Optical Character Recognition 

This project accepts various courier images and extracts the 'AWB' field from the images

## Dependencies

This project is built in python and uses [Tesseract library](https://github.com/tesseract-ocr/tesseract) for OCR. Since Tesseract is not exclusive to python, we have to install pytesseract to make it work with python


## Installation

To run this project locally, first you need to have python, pip and tesseract installed.

Links : 

- [Python](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html)
  


Then you need to set the tesseract enviroment variable to be able to use the 'tesseract' command.
  
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




## Fallback

Normal Optical Character Recognition runs only on a subset of the sample input, precicesly only on those images where the contrast between the text color and the background is high.  

To tackle this problem, when the contrast between the text and the background is very low, we can use [ImageMagick](https://imagemagick.org/index.php) library.

Using the library, we can provide the color of the text that we want to read, and the library will convert all the pixels apart from the ones containing the color we provided, to black. 

This will make it easier for tesseract to read text. 

Essentially, we can use this library to read text of a particular color
## Installation of ImageMagick Library

    1. First you can install the library from [here](https://imagemagick.org/script/download.php).
    2. After downloading the library, install it. 
    3. Then you need to set the path environment variable. To set the environment variable, you can follow the instructions stated above. 

Command to convert an image : 

```cmd
  magick {arg1} -fill {arg2} -fuzz {arg3}% +opaque {arg4} {arg5}
```
There are a total of 5 arguments that we have to pass in this command. 
They are as follows : 

    1. arg1 : 
        . Type : Path
          You have to provide the path of the image that you want to convert

    2. arg2 : 
        . Type : Color(Name / Hexcode)
          You have to provide the color that you want the background to get converted into. Black is recommended.

    3. arg3 : 
       . Type : Integer
       . Range : 1-100 Inclusive
       This property provides the fuzz value. This value defines how strict/lenient you want the conversion to be.
       Recommended Value : 20 

    4. arg4 : 
        . Type : Color(Name / Hexcode)
        You have to provide the color of the text that you want to read

    5. arg5 : 
        .Type : Path
        You have to provide the path where you want to store the converted image

Note : Insert the values without the curly brackets. 
Example of command :  
```cmd
  magick input_image.jpg -fill black -fuzz 20% +opaque blue output.jpg
```
       
## Demo

Let's take a sample image and try to run normal ocr and ocr after using magick library.

![Input Image : ](/all_images/Aramex_Sample.jpg) 

We are trying to read the text in the top left corner of the image. We can see the output generated using the following command : 

```cmd
  tesseract all_images/Aramex_Sample.jpg stdout
```

This will not give a proper output as you can see the contrast is not strong and there is overlap.

So we can first convert the image using the ImageMagick library and then run ocr on that image.

The color that we are trying to read has the hex code #d0bc40

Command : 
```cmd
  magick all_images/Aramex_Sample.jpg -fill black -fuzz 20% +opaque #d0bc40 converted/op1.jpg
```

![Output Image : ](/converted/op1.jpg) 

As you can see, in the converted image, the background has turned to black and only the text haivng hex code #d0bc40 or similar is visible. 
