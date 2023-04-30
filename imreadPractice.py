import cv2

image = cv2.imread('road.jpg')

(r, g, b) = image[100, 100]

roi = image[100:500, 100:500]

(h, w) = image.shape[:2]

ratio = 800/w

resized_image = cv2.resize(image, (800, int(ratio * h)))

#print(resized_image)

output = image.copy()

rotation_frame = cv2.getRotationMatrix2D((h//2, w//2), 45, 2)

rotated_image = cv2.warpAffine(output, rotation_frame, (w, h))

rect_image = cv2.rectangle(output, (50, 50), (100, 100), (255, 0, 0), 2)

text_image = cv2.putText(image, 'this is the example text', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

print(image.shape)
print(resized_image.shape)
#print(rotation_frame.shape)
print(rotated_image.shape)
print(rect_image.shape)
print(text_image.shape)
