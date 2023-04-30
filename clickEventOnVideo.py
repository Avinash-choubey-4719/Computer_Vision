import cv2

def click_event(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, ' ', y)
		
		cv2.putText(image, str(x) + ' ' + str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
		cv2.imshow('image', image)
	elif event == cv2.EVENT_RBUTTONDOWN:
		print(x, ' ', y)
		
		b, g, r = image[x, y]
		cv2.putText(image, str(b) + ' ' + str(g) + ' ' + str(r), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
		cv2.imshow('image', image)
		
image = cv2.imread('soniaLove.jpeg', 1)
cv2.imshow('image', image)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows() 
