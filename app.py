import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# print(f'openai_key: {api_key}' )

# Set the API key for the Google Gemini API
genai.configure(api_key=api_key)

# select the model to use
model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')

prompt = "Write a python script that generates a random number between 1 and 10."
response = model.generate_content(prompt)
print(response.text)

