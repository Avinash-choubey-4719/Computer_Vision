import cv2
import numpy as np

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

edge_image = cv2.Canny(image, 100, 200)
cv2.imshow('image', edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
