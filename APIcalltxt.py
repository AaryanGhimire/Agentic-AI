import google.generativeai as genai

# 1. Configure your API key
genai.configure(api_key="AIzaSyBhHVuSep-tayfxHIE_Cit9VKpIh-oru40")

# 2. Load the Gemini model (latest recommended)
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. Make a simple text request
response = model.generate_content("Write a short motivational quote.")

print(response.text)
