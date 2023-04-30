import cv2
import numpy as np

image = cv2.imread('soniaLove.jpeg', 1)

h , w  = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

cv2.imshow('image', image)
cv2.waitKey(0)

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grey_image = cv2.Canny(grey_image, 50, 100, apertureSize = 3)

cv2.imshow('image', grey_image)
cv2.waitKey(0)

lines = cv2.HoughLines(grey_image, 1, np.pi/180, 200)

for r_theta in lines:
	arr = np.array(r_theta[0], np.float64)
	
	r, theta = arr

	a = np.cos(theta)
	b = np.sin(theta)
	
	x0 = a*r
	y0 = b*r
	
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	
	cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 1)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
