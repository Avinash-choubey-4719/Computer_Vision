import cv2
import numpy as np
import matplotlib.pyplot as plt


def highContrast(image, r1, s1, r2, s2):
	if(image >= 0) and (image <= r1):
		return ((s1 - 0)/(r1 - 0)) * (image + 0) + 0
	elif(image > r1) and (image <= r2):
		return ((s2 - s1)/(r2 - r1)) * (image - r1) + s1
	else:
		return ((255 - s2)/(255 - r2)) * (image - r2) + s2


image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

function = np.vectorize(highContrast)

contrast_image = function(image, 70, 0, 140, 255)
cv2.imshow('image', contrast_image)
cv2.waitKey(0)

plt.imshow(contrast_image)
plt.waitforbuttonpress()
plt.close('all')

cv2.destroyAllWindows()
