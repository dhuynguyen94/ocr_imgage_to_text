import cv2
import numpy as np
import pytesseract
from PIL import Image
import re
import os
import argparse
import glob
from PIL import Image


# Define image for filtering noise and tracking the text
def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Creating the Kernel for Convolutional Technical 
    kernel = np.ones((1, 1), np.uint8)
    # Apply dilation and erosion to remove some noise
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img)
    print(result)
    return result


# Function to extract all the numbers from the given string
def getNumbers(str):
    # array = re.findall(r'[\d]+', str)
    array = re.findall(r'[0-9]+', str)
    # array = re.findall(r'(?<!\d)\d{13}(?!\d)', str)
    # array = re.findall(r'^[0-9A-Z_-]*$', str)
    return array


# Function to save Test's ID to txt file
def saving_test_id(path: str, id: int):
    if os.path.isfile(path):
        file = open(path, "r")
        previous_race_id = int(file.readline())
    else:
        with open(path, "w") as myfile:
            myfile.write(str(id))


def ocr_img2text(img_path, id_leng: int):
    # Driver code
    print ('--- Start recognize text from image ---')
    my_txt = get_string(img_path)
    print ("------ Done Extracting from Img to Text-------")
    
    # Saving all of number to Array for checking
    array = getNumbers(my_txt)
    print ("------ Array of Digits-------")
    print(array)

    # Selecting test ID 
    test_id = 0 
    for i in array:
        if len(i) == int(id_leng): 
            test_id = int(i)
    print(f"Test ID is: {test_id}")
    return test_id
    # Saving to Test_ID text file
    # saving_test_id("test_id.txt", test_id)


if __name__ == "__main__":

    id_leng = 6
    # Test with one image sample named 1391.png
    images = glob.glob("1391.png")
    # Test with Full Data
    # images = glob.glob("data_full/*.png")
    for image in images:
        # print(image)
        # with open(image, 'rb') as file:
            # img = Image.open(file)
        ocr_img2text(image, id_leng)
        print(image)








