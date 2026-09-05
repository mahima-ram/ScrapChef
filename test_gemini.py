import os

from dotenv import load_dotenv
from google import genai


# Load our .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY was not found.")
    exit()


# Create the Gemini client
client = genai.Client(
    api_key=api_key
)


# Ask Gemini a simple question
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Give me one short vegetarian dinner idea."
)


print()
print("🤖 Gemini says:")
print(response.text)
