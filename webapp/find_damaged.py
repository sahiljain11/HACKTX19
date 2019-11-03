import requests
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
endpoint = 'https://image-classification.cognitiveservices.azure.com/'
prediction_key = 'ba8e403c3f904d85adf408928b13fa90'
predictor = CustomVisionPredictionClient(prediction_key, endpoint=endpoint)
iteration_id = 'e6e60cf8-b68c-46a2-a5e5-fe015196bf89'
project_id = '2744fc95-61ce-4f3a-a4d6-e0fad1647c9c'


MIN_BOX_SIZE = 5       #10x10

BIG_IMAGE_SCALE_VALUE = 4
def generateBox(satellite_image, x_size, y_size):
    scale = 5
    result = []
    for y in range(0, y_size, int(y_size / scale)):
        row = []
        for x in range(0, x_size, int(x_size / scale)):
            if y + scale < y_size and x + scale < x_size :
                area = (x, y, x + int(x_size / scale), y + int(y_size / scale))
                shrunk_image = satellite_image.crop(area)
                row.append(shrunk_image)
        result.append(row)

    return result

def find_damage(image):
    pil_image = Image.open(image)
    x,y = pil_image.size
    image_names = generateBox(pil_image,x,y)
    result_matrix = []
    for row in image_names[0:-1]:
        row_result = []
        for image in row: 
            with BytesIO() as output:
                image.save(output,'BMP')
                bytesdata = output.getvalue()
            result = predictor.classify_image(project_id,'Iteration4',bytesdata)
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
    for row in range(0,4):
        x = 0
        new_row = Image.new('RGB',(total_x,y_size))
        for col in range(0,4):
            square = section_matrix[row][col]
            if damage_matrix[row][col] == 1:
                draw = ImageDraw.Draw(square,'RGBA')
                draw.rectangle(((0,0),(x_size,y_size)),fill = (255,0,0,100) , outline = None)
            new_row.paste(square,(x,0))
            x+=x_size
        new_image.paste(new_row,(0,y))
        y+=y_size
    return new_image