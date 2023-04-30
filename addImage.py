import cv2

image1 = cv2.imread('sonia.jpeg', 1)
image2 = cv2.imread('road.jpg', 1)

image1 = cv2.resize(image1, (800, 800))
image2 = cv2.resize(image2, (800, 800))

output = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

h, w = output.shape[:2]
ratio = 500/w

output = cv2.resize(output, (500, int(ratio * h)))

cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
