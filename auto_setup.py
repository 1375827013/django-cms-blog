import requests
import time
import json

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

print("=== 步骤 1: 关闭所有旧控制台 ===")
consoles_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.get(consoles_url, headers=headers)
if response.status_code == 200:
    consoles = response.json()
    for console in consoles:
        kill_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console['id']}/"
        requests.delete(kill_url, headers=headers)
        print(f"  关闭控制台 {console['id']}")
    time.sleep(1)

print("\n=== 步骤 2: 创建新控制台 ===")
create_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.post(create_url, headers=headers, json={
    "executable": "/bin/bash"
})

if response.status_code not in [200, 201]:
    print(f"创建失败: {response.text}")
    exit(1)

console_data = response.json()
console_id = console_data["id"]
print(f"  控制台 ID: {console_id}")

print("\n=== 步骤 3: 发送命令 ===")
commands = [
    "cd /home/8210232126/django-cms-blog",
    "git fetch origin",
    "git reset --hard origin/main",
    "source myenv/bin/activate",
    "python manage.py migrate --run-syncdb",
    "python manage.py createadmin",
    "echo 'DONE'"
]

for cmd in commands:
    input_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
    r = requests.post(input_url, headers=headers, json={"input": cmd + "\n"})
    print(f"  发送: {cmd}")
    time.sleep(0.5)

print("\n=== 步骤 4: 等待执行 (15秒) ===")
for i in range(15, 0, -1):
    print(f"  等待 {i} 秒...", end="\r")
    time.sleep(1)
print()

print("\n=== 步骤 5: 检查输出 ===")
output_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/get_latest_output/"
r = requests.get(output_url, headers=headers)
if r.status_code == 200:
    output = r.json().get("output", "")
    if "DONE" in output:
        print("  ✅ 命令执行完成!")
    print("\n--- 输出内容 ---")
    lines = output.split("\n")
    for line in lines[-30:]:
        print(line)
else:
    print(f"  获取输出失败: {r.text}")

print("\n=== 步骤 6: 重载网站 ===")
reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
r = requests.post(reload_url, headers=headers)
print(f"  重载状态: {r.status_code}")

print("\n" + "="*50)
print("✅ 全部完成!")
print("="*50)
print("\n用户名: admin")
print("密码: admin123456")
print("\n登录地址: https://8210232126.pythonanywhere.com/admin/login/")
