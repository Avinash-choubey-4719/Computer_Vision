import numpy as np
import cv2

image = cv2.imread('soniaLove.jpeg', 0)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w *h)))

hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])

import matplotlib.pyplot as plt

plt.plot(hist_image)
plt.show()

plt.hist(image.ravel(), 256, [0, 256])
plt.show()
