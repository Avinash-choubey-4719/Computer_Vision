import cv2

image = cv2.imread('road.jpg')

#print(image.shape)
#print(image)

h, w = image.shape[:2]

(b, g, r) = image[100, 100]

#print(b, g, r)

b = image[100, 100, 0]
#print(b)

roi = image[100:500, 100:500]
#print(roi.shape)

#print(h, w)

resized_image = cv2.resize(image, (800, 800))
#print(resized_image.shape)

ratio = 800/w
new_image = cv2.resize(image, (800, int(ratio * h)))
#print(new_image.shape)

center = (h//2, w//2)

temp_rotated_image = cv2.getRotationMatrix2D(center, -45, 1)
rotated_image = cv2.warpAffine(image, temp_rotated_image, (w, h))
#print(rotated_image.shape)

output = image.copy()

rect_image = cv2.rectangle(output, (50, 50), (100, 100), (255, 0, 0), 4)
#print(rect_image.shape)

text_image = cv2.putText(output, "this is the text on the image", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
print(text_image.shape)
