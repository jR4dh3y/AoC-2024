from PIL import Image
import requests
from io import BytesIO
from rembg import remove

# Load the image
input_path = "a.jpg"
output_path = "no_bg.png"

# Remove background
with open(input_path, "rb") as input_file:
    input_image = input_file.read()
    output_image = remove(input_image)

# Save the output
with open(output_path, "wb") as output_file:
    output_file.write(output_image)

output_path
