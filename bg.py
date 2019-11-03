import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('test.png')

image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)

lower_blue = np.array([0, 255, 0])##[R value, G value, B value]
upper_blue = np.array([120, 255, 100])

mask = cv2.inRange(image_copy, lower_blue, upper_blue)
plt.imshow(mask, cmap='gray')

plt.show()