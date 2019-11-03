from PIL import Image

BIG_IMAGE_SCALE_VALUE = 4
MIN_BOX_SIZE = 10       #10x10

def generateBox(satellite_image, x_size, y_size):
    temp = x_size / MIN_BOX_SIZE
    if temp < y_size / MIN_BOX_SIZE:
        temp = y_size / MIN_BOX_SIZE
    for scale in range(int(temp), BIG_IMAGE_SCALE_VALUE, -2):
        for y in range(0, y_size, int(y_size / scale)):
            for x in range(0, x_size, int(x_size / scale)):
                if y + scale < y_size and x + scale < x_size :
                    area = (x, y, x + int(x_size / scale), y + int(y_size / scale))
                    shrunk_image = satellite_image.crop(area)
                    shrunk_image.save(str(scale) + "s" + str(x) + "x" + str(y) + "y" +
                                      "cropped.png", "PNG", optimize=True)

img = Image.open('test.png')
generateBox(img, img.size[0], img.size[1])
