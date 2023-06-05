import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://excelcopilot.azurewebsites.net/api/openai_completion'

params = {
    'prompt': 'Hello',
    'engine': 'text-davinci-003',
    'temperature': 0.7,
    'max_tokens': 30,
    'verbose': False
}

headers = {
    'x-functions-key': os.getenv("EXCELCOPILOT_KEY")    
}

response = requests.get(url, headers=headers, params=params)

print("Status code:", response.status_code)
print("Response content:", response.text)

try:
    print("Parsed JSON:", response.json())
except ValueError:
    print("Could not parse JSON")
