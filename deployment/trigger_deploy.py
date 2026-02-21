import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {'Authorization': f"Token {os.getenv('DEPLOY_TOKEN', '')}"}
r = requests.post('https://8210232126.pythonanywhere.com/deploy/', headers=headers, timeout=60)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")
