import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
DEPLOY_TOKEN = "X7k9pQ2mR4vL8nJ3wT6yB5eA1cD9fG0h"

print("触发部署 webhook...")
webhook_url = f"https://{PA_USERNAME}.pythonanywhere.com/deploy/"
headers = {
    "Authorization": f"Token {DEPLOY_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, headers=headers)

print(f"状态码: {response.status_code}")
print(f"响应: {response.text}")

if response.status_code == 200:
    print("\n✅ 部署成功!")
    print("\n用户名: admin")
    print("密码: admin123456")
    print("\n登录地址: https://8210232126.pythonanywhere.com/admin/login/")
