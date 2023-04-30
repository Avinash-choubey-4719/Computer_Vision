import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

ellipse_image = cv2.ellipse(image, (50, 50), (100, 50), 50, 0, 360, (0, 255, 0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.imshow('image', ellipse_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
