import cv2

image = cv2.imread('sonia.jpeg', 1)

output = image.copy()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]

resized_image = cv2.resize(image, (800, int(800/w * h)))

cv2.imshow('image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import matplotlib.pyplot as plt

plt.imshow(output)
plt.waitforbuttonpress()
plt.close('all')
