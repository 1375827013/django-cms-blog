import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"

headers = {"Authorization": f"Token {PA_API_TOKEN}"}

api_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
response = requests.post(api_url, headers=headers)

print(f"重载状态: {response.status_code}")
print(f"响应: {response.text}")

if response.status_code == 200:
    print("\n✅ 网站已重载！")
    print("\n请稍等几秒后访问以下链接创建管理员：")
    print("https://8210232126.pythonanywhere.com/create-admin/")
