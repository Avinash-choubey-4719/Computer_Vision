import cv2

image = cv2.imread('soniaLove.jpeg', 1)

h, w = image.shape[:2]

image = cv2.resize(image, (500, int(500/w * h)))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, otsu_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('image', otsu_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
