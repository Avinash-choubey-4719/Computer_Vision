import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

arrow_image = cv2.arrowedLine(image, (0, 0), (255, 255), (0, 255, 0), 5, tipLength = 0.1)

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.imshow('image', arrow_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
