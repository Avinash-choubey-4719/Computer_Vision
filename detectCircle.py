import cv2
import numpy as np

image = cv2.imread('sonia.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur_image = cv2.blur(image, (3,3))

circles = cv2.HoughCircles(blur_image, cv2.HOUGH_GRADIENT, 1, 20, 100, 200, 1, 40)

if circles is not None:
	circles = np.uint16(np.around(circles))
	
	for pt in circles[0, :]:
		x, y, r = pt
		cv2.circle(image, (x, y), r, (0, 255, 0), 3)

cv2.imshow('image', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
