import requests

url = "https://8210232126.pythonanywhere.com/create-admin/"
response = requests.get(url)

print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")
