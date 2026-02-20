import requests
import time

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

print("1. 创建控制台...")
console_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
console_response = requests.post(
    console_url,
    headers=headers,
    json={"executable": "bash", "working_directory": f"/home/{PA_USERNAME}/django-cms-blog"}
)
print(f"   状态码: {console_response.status_code}")

if console_response.status_code in [200, 201]:
    console_data = console_response.json()
    console_id = console_data["id"]
    print(f"   控制台 ID: {console_id}")
    
    print("\n2. 等待控制台就绪...")
    time.sleep(2)
    
    print("\n3. 发送 collectstatic 命令...")
    send_command_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
    commands = [
        "source /home/8210232126/.virtualenvs/myvirtualenv/bin/activate\n",
        "cd /home/8210232126/django-cms-blog\n",
        "python manage.py collectstatic --noinput\n",
        "echo '=== DONE ==='\n"
    ]
    
    for cmd in commands:
        requests.post(send_command_url, headers=headers, json={"input": cmd})
        time.sleep(1)
    
    print("   命令已发送！")
    print("\n⏳ 请等待 10-15 秒让 collectstatic 完成...")
    time.sleep(15)
    
    print("\n4. 重载网站...")
    reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
    reload_response = requests.post(reload_url, headers=headers)
    print(f"   重载状态码: {reload_response.status_code}")
    
    print("\n" + "="*50)
    print("✅ 完成！")
    print(f"访问地址: https://{PA_USERNAME}.pythonanywhere.com/admin/")
    print("\n如果样式还没显示，请等待几秒后刷新页面！")
else:
    print(f"❌ 创建控制台失败")
    print(f"响应: {console_response.text}")
