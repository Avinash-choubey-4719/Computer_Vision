import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

border_const = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value = 1)
cv2.imshow('image', border_const)
cv2.waitKey(0)

border_reflect = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_REFLECT)
cv2.imshow('image', border_reflect)
cv2.waitKey(0)

border_default = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_DEFAULT)
cv2.imshow('image', border_default)
cv2.waitKey(0)

border_replicate = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_REPLICATE)	
cv2.imshow('image', border_replicate)
cv2.waitKey(0)
