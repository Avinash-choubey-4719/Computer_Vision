import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))
cv2.imshow('image', image)
cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
