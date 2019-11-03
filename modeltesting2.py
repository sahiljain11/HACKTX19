# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:43:00 2019

@author: Danie
"""
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
endpoint = 'https://image-classification.cognitiveservices.azure.com/'
prediction_key = 'ba8e403c3f904d85adf408928b13fa90'
predictor = CustomVisionPredictionClient(prediction_key, endpoint=endpoint)
project_id = '2744fc95-61ce-4f3a-a4d6-e0fad1647c9c'


BIG_IMAGE_SCALE_VALUE = 4
def generateBox(satellite_image, x_size, y_size):
    scale = 5
    result = []
    i = 0
    for y in range(0, y_size, int(y_size / scale)):
        row = []
        for x in range(0, x_size, int(x_size / scale)):
            if y + scale < y_size and x + scale < x_size :
                area = (x, y, x + int(x_size / scale), y + int(y_size / scale))
                shrunk_image = satellite_image.crop(area)
                filename = "cropped({}).png".format(i)
                shrunk_image.save(filename, "PNG", optimize=True)
                row.append(filename)
                i+=1
        result.append(row)

    return result

def find_damage(image):
    pil_image = image
    x,y = pil_image.size
    image_names = generateBox(pil_image,x,y)
    result_matrix = []
    for row in image_names[0:-1]:
        row_result = []
        for name in row: 
            result = predictor.classify_image(project_id,'Iteration4',open(name,'rb').read())
            damaged_probability = 0.0
            for prediction in result.predictions:
                if prediction.tag_name == 'damaged':
                    damaged_probability = prediction.probability
            if damaged_probability > 0.5:
                row_result.append(True)
            else:
                row_result.append(False)
        result_matrix.append(row_result)
    new_image = combineimage(image_names,result_matrix,x,y)
    return new_image

def combineimage(section_matrix,damage_matrix,total_x,total_y):
    x_size = int(total_x/5)
    y_size = int(total_y/5)
    new_image = Image.new('RGB',(total_x,total_y))
    x = 0
    y = 0
    for row in range(0,5):
        x = 0
        new_row = Image.new('RGB',(total_x,y_size))
        for col in range(0,5):
            square = Image.open(section_matrix[row][col]).convert('RGB')
            if damage_matrix[row][col] == 1:
                draw = ImageDraw.Draw(square,'RGBA')
                draw.rectangle(((0,0),(x_size,y_size)),fill = (255,0,0,100) , outline = None)
            new_row.paste(square,(x,0))
            x+=x_size
        new_image.paste(new_row,(0,y))
        y+=y_size
    return new_image
            

with Image.open("C:\\Users\\Danie\\hacktx2019training2\\post_damage\\hurricane-florence_00000001_post_disaster.png") as image:
    result = find_damage(image)
    result.save('anewimage.png')
