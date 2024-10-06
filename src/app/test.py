import requests

try:
    response = requests.get("http://host.docker.internal:11434")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Connection failed: {e}")
