import requests
import json

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"

console_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

response = requests.post(console_url, headers=headers, json={
    "executable": "bash"
})

if response.status_code == 201:
    console_data = response.json()
    console_id = console_data["id"]
    print(f"✅ 控制台创建成功，ID: {console_id}")
    
    commands = [
        "cd /home/8210232126/django-cms-blog",
        "git fetch origin",
        "git reset --hard origin/main",
        "source myenv/bin/activate",
        "python create_admin.py"
    ]
    
    for cmd in commands:
        input_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
        requests.post(input_url, headers=headers, json={"input": cmd + "\n"})
        print(f"执行: {cmd}")
    
    print("\n✅ 命令已发送！请稍等几秒钟后尝试登录。")
    print(f"\n用户名: admin")
    print(f"密码: admin123456")
else:
    print(f"❌ 创建控制台失败: {response.text}")
