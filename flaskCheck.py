import requests
import json
import base64

url = 'http://10.3.5.96:8080/' # Replace with your Flask API endpoint
filename = 'sonia.jpeg' # Replace with your sample image file

# Encode the image file to base64
with open(filename, 'rb') as f:
    encoded_image = base64.b64encode(f.read()).decode('utf-8')

# Create the JSON request body
request_body = {
    'image': encoded_image
}

# Send HTTP POST request with the JSON request body
response = requests.post(url, data=json.dumps(request_body), headers={'Content-Type': 'application/json'})

# Print the response from the Flask API
print(response.content)
print(response.json())
