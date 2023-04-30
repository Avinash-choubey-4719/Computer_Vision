import cv2
import numpy as np

image = cv2.imread('soniaLove.jpeg', 0)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

cv2.imshow('image', image)
cv2.waitKey(0)

ret, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow('image', image)
cv2.waitKey(0)

kernel = np.ones((5, 5), np.uint8)

image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations = 2)

image = cv2.dilate(image, kernel, iterations = 1)

image = cv2.distanceTransform(image, cv2.DIST_L2, 0)
ret, image = cv2.threshold(image, 0.02 * image.max(), 255, 0)
cv2.imshow('image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
