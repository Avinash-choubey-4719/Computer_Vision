import cv2

image = cv2.imread('road.jpg', 1)

(h, w) = image.shape[:2]

ratio = 800/w

image = cv2.resize(image, (800, int(ratio * h)))

cv2.imshow('image', image)

cv2.waitKey(0)

cv2.destroyAllWindows()

#print("printing after the execution")

roi = image[50:100, 50:100]

cv2.imshow('image', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

rect_image = cv2.rectangle(image, (50, 50), (100, 100), (255, 0, 0), 4)

cv2.imshow('image', rect_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

text_image = cv2.putText(rect_image, 'this is the text', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 3)
cv2.imshow('image', text_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import matplotlib.pyplot as plt

plt.imshow(image)
plt.waitforbuttonpress()
plt.close('all')
