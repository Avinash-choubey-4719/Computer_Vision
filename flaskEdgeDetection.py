from flask import Flask, request, jsonify
import cv2
import numpy
import base64


def process_image_function(img):
	
 
	# Read the original image
	#img = cv2.imread('soniaLove.jpeg') 

	h, w = img.shape[:2]

	img = cv2.resize(img, (500, int(500/w * h)))

	# Display original image
	#cv2.imshow('Original', img)
	#cv2.waitKey(0)

	# Convert to graycsale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Blur the image for better edge detection
	img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
	# Sobel Edge Detection
	sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
	sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
	sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
	# Display Sobel Edge Detection Images
	#cv2.imshow('Sobel X', sobelx)
	#cv2.waitKey(0)
	#cv2.imshow('Sobel Y', sobely)
	#cv2.waitKey(0)
	#cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
	#cv2.waitKey(0)
 
	# Canny Edge Detection
	edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
	# Display Canny Edge Detection Image
	#cv2.imshow('Canny Edge Detection', edges)
	#cv2.waitKey(0)
 
	#cv2.destroyAllWindows()
	
	return edges

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def process_image():
	if request.method == 'GET':
		#img = cv2.imread('soniaLove.jpeg', 1)
		#processed_image = process_image_function(img)
		#_, img_encoded = cv2.imencode('.png', processed_image)
		#img_base64 = base64.b64encode(img_encoded).decode('utf-8')
		#return jsonify({'image':img_base64})
		return 'hello world'
	elif request.method == 'POST':
		#image_data = request.files['image']
		data = request.get_json()
		#print(data)
		encoded_image = data['image']
		#print(encoded_image)
		#encoded_image = image_data.read()
		decoded_image = base64.b64decode(encoded_image)
		img = cv2.imdecode(numpy.frombuffer(decoded_image, numpy.uint8), cv2.IMREAD_COLOR)
		#img = cv2.imread('soniaLove.jpeg', 1)
		processed_image = process_image_function(img)
		#print(processed_image.shape)
		_, img_encoded = cv2.imencode('.png', processed_image)
		img_base64 = base64.b64encode(img_encoded).decode('utf-8')
		return jsonify({'image':img_base64})
		
if __name__ == '__main__':
	app.run(debug = True)
