import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

ret, bin_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
ret, bin_env_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
ret, trunc_image = cv2.threshold(image, 150, 255, cv2.THRESH_TRUNC)
ret, zero_image = cv2.threshold(image, 150, 255, cv2.THRESH_TOZERO)
ret, zero_inv_image = cv2.threshold(image, 150, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('image', image)
#cv2.waitKey(0)
cv2.imshow('image', bin_image)
#cv2.waitKey(0)
cv2.imshow('image', bin_env_image)
#cv2.waitKey(0)
cv2.imshow('image', trunc_image)
#cv2.waitKey(0)
cv2.imshow('image', zero_image)
#cv2.waitKey(0)
cv2.imshow('image', zero_inv_image)
#cv2.waitKey(0)


if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
