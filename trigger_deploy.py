import requests

headers = {'Authorization': 'Token X7k9pQ2mR4vL8nJ3wT6yB5eA1cD9fG0h'}
r = requests.post('https://8210232126.pythonanywhere.com/deploy/', headers=headers, timeout=60)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")
