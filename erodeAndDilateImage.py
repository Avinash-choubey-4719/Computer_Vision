import cv2
import numpy as np

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

kernel = np.ones((5, 5), np.uint8)

erode_image = cv2.erode(image, kernel, iterations = 1)
dilate_image = cv2.dilate(image, kernel, iterations = 1)

cv2.imshow('image', erode_image)
cv2.waitKey(0)

cv2.imshow('image', dilate_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
