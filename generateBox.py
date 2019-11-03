BIG_IMAGE_SCALE_VALUE = 4
MIN_BOX_SIZE = 10

def generateBox(satellite_image, x_size, y_size):
    for scale in range(BIG_IMAGE_SCALE_VALUE, x_size / 10, 2):
        for y in range(0, y_size, scale):
            for x in range(0, x_size, scale):
                shrunk_image = 
