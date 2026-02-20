import requests
import time

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

task_command = """
cd /home/8210232126/django-cms-blog
source myenv/bin/activate
git fetch origin
git reset --hard origin/main
python manage.py migrate --run-syncdb
python manage.py createadmin
"""

tasks_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/schedule/"

print("检查现有任务...")
response = requests.get(tasks_url, headers=headers)
if response.status_code == 200:
    tasks = response.json()
    print(f"找到 {len(tasks)} 个任务")
    for task in tasks:
        print(f"  - ID: {task['id']}, 命令: {task['command'][:50]}...")

print("\n创建新任务...")
response = requests.post(tasks_url, headers=headers, json={
    "command": "cd /home/8210232126/django-cms-blog && source myenv/bin/activate && git fetch origin && git reset --hard origin/main && python manage.py migrate --run-syncdb && python manage.py createadmin",
    "hour": 0,
    "minute": 0,
    "enabled": True
})

if response.status_code in [200, 201]:
    task_data = response.json()
    task_id = task_data['id']
    print(f"✅ 任务创建成功，ID: {task_id}")
    print("\n请到 PythonAnywhere 控制台手动运行任务，或者等待定时执行")
    print(f"任务列表: https://www.pythonanywhere.com/user/{PA_USERNAME}/schedule_tab/")
else:
    print(f"创建任务失败: {response.text}")
