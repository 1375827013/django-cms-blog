import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

tasks_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/schedule/"

print("检查现有任务...")
response = requests.get(tasks_url, headers=headers)
if response.status_code == 200:
    tasks = response.json()
    for task in tasks:
        print(f"  删除任务 {task['id']}")
        delete_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/schedule/{task['id']}/"
        requests.delete(delete_url, headers=headers)

print("\n创建新任务...")
command = "cd /home/8210232126/django-cms-blog && source myenv/bin/activate && git fetch origin && git reset --hard origin/main && python manage.py migrate --run-syncdb && python manage.py createadmin"

response = requests.post(tasks_url, headers=headers, json={
    "command": command,
    "hour": 0,
    "minute": 0,
    "enabled": True
})

if response.status_code in [200, 201]:
    task = response.json()
    print(f"✅ 任务创建成功!")
    print(f"   ID: {task['id']}")
    print(f"   命令: {task['command'][:60]}...")
    print(f"\n请访问以下链接查看并运行任务:")
    print(f"https://www.pythonanywhere.com/user/{PA_USERNAME}/schedule_tab/")
else:
    print(f"创建失败: {response.status_code}")
    print(response.text)
