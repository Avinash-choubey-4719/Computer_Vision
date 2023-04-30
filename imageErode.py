import cv2
import numpy as np

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

kernel = np.ones((3, 3), np.uint8)
print(kernel)

erode_image = cv2.erode(image, kernel, cv2.BORDER_CONSTANT)

cv2.imshow('image', erode_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
