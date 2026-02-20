import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"

headers = {"Authorization": f"Token {PA_API_TOKEN}"}

consoles_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
response = requests.get(consoles_url, headers=headers)

if response.status_code == 200:
    consoles = response.json()
    print(f"找到 {len(consoles)} 个控制台")
    
    for console in consoles:
        console_id = console["id"]
        print(f"控制台 ID: {console_id}")
        
        commands = [
            "cd /home/8210232126/django-cms-blog",
            "git fetch origin",
            "git reset --hard origin/main",
            "source myenv/bin/activate",
            "python create_admin.py"
        ]
        
        for cmd in commands:
            input_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
            r = requests.post(input_url, headers=headers, json={"input": cmd + "\n"})
            print(f"执行: {cmd} - 状态: {r.status_code}")
        
        break
else:
    print(f"获取控制台失败: {response.text}")
