import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

guass_image = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('image', guass_image)
cv2.waitKey(0)

med_image = cv2.medianBlur(image, 5)
cv2.imshow('image', med_image)
cv2.waitKey(0)

bilate_image = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('image', bilate_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
