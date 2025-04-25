import requests
import json

# URL and authentication credentials
url = "https://nodemand.las.iastate.edu/ollama/api/generate"
username = "tracweb-education"
password = "30ee7378779e49a6a2471f8b"

# Request payload
payload = {
    "model": "deepseek-r1:70b",
    "prompt": "list the funniest atomic element names",
    "stream": False
}

# Make the POST request with basic authentication
response = requests.post(
    url,
    auth=(username, password),
    json=payload  # automatically converts to JSON and sets content-type header
)

# Check if the request was successful
if response.status_code == 200:
    # Parse and print the response
    result = response.json()
    print(result['response'])
    
else:
    print(f"Error: {response.status_code}")
    print(response.text)