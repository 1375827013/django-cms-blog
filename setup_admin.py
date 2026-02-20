import requests
import time

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

consoles_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.get(consoles_url, headers=headers)

if response.status_code == 200:
    consoles = response.json()
    if consoles:
        console_id = consoles[0]['id']
        print(f"使用控制台 ID: {console_id}")
        
        kill_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/"
        requests.delete(kill_url, headers=headers)
        print("已关闭旧控制台")
        time.sleep(2)

create_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.post(create_url, headers=headers, json={
    "executable": "/bin/bash"
})

if response.status_code in [200, 201]:
    console_data = response.json()
    console_id = console_data["id"]
    print(f"✅ 新控制台创建成功，ID: {console_id}")
    
    commands = [
        "cd /home/8210232126/django-cms-blog",
        "git fetch origin",
        "git reset --hard origin/main",
        "source myenv/bin/activate",
        "python manage.py migrate",
        "python create_admin.py"
    ]
    
    for cmd in commands:
        input_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
        r = requests.post(input_url, headers=headers, json={"input": cmd + "\n"})
        print(f"执行: {cmd}")
        time.sleep(1)
    
    print("\n✅ 命令已发送！")
    print("\n用户名: admin")
    print("密码: admin123456")
    print("\n请等待约 10 秒后尝试登录:")
    print("https://8210232126.pythonanywhere.com/admin/login/")
else:
    print(f"❌ 创建控制台失败: {response.status_code}")
    print(response.text)
