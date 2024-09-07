import requests
from PIL import Image
from io import BytesIO

API_KEY = 'YOUR API'  # Replace with your actual API key
API_URL = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={API_KEY}'

response = requests.get(API_URL)
data = response.json()

if not data:
    print("No data received from the API.")
    exit()

latest_image = data[0]
image_date = latest_image['date'].split()[0].replace('-', '/')
image_name = latest_image['image']

image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={API_KEY}'
print(f"Image URL: {image_url}")

image_response = requests.get(image_url)
if image_response.status_code != 200:
    print(f"Failed to download image. Status code: {image_response.status_code}")
    exit()

image = Image.open(BytesIO(image_response.content))
image.show()
