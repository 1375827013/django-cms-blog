import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

files_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/files/path/home/{PA_USERNAME}/django-cms-blog/app_name/management/commands/"

print("检查服务器上的文件...")
response = requests.get(files_url, headers=headers)

if response.status_code == 200:
    print("✅ management/commands 目录存在")
    print(response.text[:500])
else:
    print(f"❌ 目录不存在或无法访问: {response.status_code}")
    print(response.text)
