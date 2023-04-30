import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('soniaLove.jpeg', 1)

cv2.imshow('image', image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w *h )))

plt.hist(image.ravel(), 256, [0, 256])
plt.show()

hist = cv2.equalizeHist(image)

plt.hist(hist.ravel(), 256, [0, 256])
plt.show()

cv2.imshow('image', hist)
cv2.waitKey(0)


resultant_image = np.hstack((image, hist))

cv2.imshow('image', resultant_image)
cv2.waitKey(0)

plt.hist(resultant_image.ravel(), 256, [0, 256])
plt.show()


cv2.destroyAllWindows()
