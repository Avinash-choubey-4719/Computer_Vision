import cv2

video = cv2.VideoCapture('cars.mp4')

while(True):
	ret, frame = video.read()
	if ret:
		cv2.imshow('image', frame)
		
		if(cv2.waitKey(25) & 0xFF == ord('q')):
			break
	else:
		print('video over')
video.release()
cv2.destroyAllWindows()
