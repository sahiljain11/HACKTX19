# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:39:23 2019

@author: Danie
"""
import requests
from PIL import Image
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
endpoint = 'https://image-classification.cognitiveservices.azure.com/'
prediction_key = 'ba8e403c3f904d85adf408928b13fa90'
predictor = CustomVisionPredictionClient(prediction_key, endpoint=endpoint)
iteration_id = 'e6e60cf8-b68c-46a2-a5e5-fe015196bf89'
project_id = '2744fc95-61ce-4f3a-a4d6-e0fad1647c9c'


BIG_IMAGE_SCALE_VALUE = 4
MIN_BOX_SIZE = 5       #10x10

def generateBox(satellite_image, x_size, y_size):
    scale = 5
    result = []
    i = 0
    j = 0
    for y in range(0, y_size, int(y_size / scale)):
        row = []
        for x in range(0, x_size, int(x_size / scale)):
            if y + scale < y_size and x + scale < x_size :
                area = (x, y, x + int(x_size / scale), y + int(y_size / scale))
                shrunk_image = satellite_image.crop(area)
                filename = "cropped({0},{1}).png".format(i,j)
                shrunk_image.save(filename, "PNG", optimize=True)
                row.append(filename)
                i+=1
        j+=1
        result.append(row)
    return result

def get_array(image):
    result = []
    pil_image = Image.frombytes(image)
    x,y = pil_image.size
    image_names = generateBox(pil_image,x,y)
    for row in image_names:
        row = []
        for name in row: 
            result = predictor.classify_image(project_id,'Iteration3',image.read())
            for prediction in result.predictions:
                damaged_probability = 0.0
                if prediction.tagName == 'damaged':
                    damaged_probability = prediction.probability
            if damaged_probability > 0.5:
                row.append(True)
            else:
                row.append(False)
        result.append(row)
    return result

            