import cv2

image = cv2.imread('sonia.jpeg', 1)

(h, w) = image.shape[:2]

ratio = 800/w

image = cv2.resize(image, (800, int(ratio * h)))

b, g, r = cv2.split(image)

cv2.imshow('image', b)
cv2.waitKey(0)

cv2.imshow('image', g)
cv2.waitKey(0)

cv2.imshow('image', r)
cv2.waitKey(0)

cv2.destroyAllWindows()
