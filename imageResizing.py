import cv2

image = cv2.imread('soniaLove.jpeg', 1)

cv2.imshow('image', image)
cv2.waitKey(0)

h, w = image.shape[:2]

resized_image = cv2.resize(image, (500, int(500/w * h)))

cv2.imshow('image', resized_image)
cv2.waitKey(0)


half_image = cv2.resize(image, (0, 0),  fx = 0.5, fy= 0.5, interpolation = cv2.INTER_LINEAR)
cv2.imshow('image', half_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
