# vision.py
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Google Gemini
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input:
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Process the image (placeholder function)
def process_image(image):
    # Implement any image pre-processing here if needed
    return image
