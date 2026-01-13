import google.generativeai as genai
from PIL import Image

# Configure API Key
genai.configure(api_key="AIzaSyBJx0WoMP7xvVeNKfyF1N3aK5q6VBsm6kw")

# Load model
# model = genai.GenerativeModel("gemini-2.5-flash")
model = genai.GenerativeModel("gemini-robotics-er-1.5-preview")


# Load an image (local file)
image = Image.open("Treble.webp")

# Send image + text prompt
response = model.generate_content(
    ["Describe this image in detail.", image]
)

# Print output
print(response.text)
