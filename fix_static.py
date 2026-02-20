import requests
import time

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

base_project_path = f"/home/{PA_USERNAME}/django-cms-blog"

def create_file(path, content):
    url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/files/path{path}"
    files = {'content': ('file', content)}
    response = requests.post(url, headers=headers, files=files)
    return response

print("=== 步骤 1: 重新上传所有文件...\n")

print("1.1 上传 admin_custom.css")
with open("static/css/admin_custom.css", "r", encoding="utf-8") as f:
    css_content = f.read()
r1 = create_file(f"{base_project_path}/static/css/admin_custom.css", css_content)
print(f"   status: {r1.status_code}")

print("\n1.2 上传 base_site.html")
with open("templates/admin/base_site.html", "r", encoding="utf-8") as f:
    base_content = f.read()
r2 = create_file(f"{base_project_path}/templates/admin/base_site.html", base_content)
print(f"   status: {r2.status_code}")

print("\n1.3 上传 index.html")
with open("templates/admin/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()
r3 = create_file(f"{base_project_path}/templates/admin/index.html", index_content)
print(f"   status: {r3.status_code}")

print("\n=== 步骤 2: 创建控制台并运行 collectstatic...\n")

console_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
console_response = requests.post(
    console_url,
    headers=headers,
    json={"executable": "bash", "working_directory": base_project_path}
)
print(f"创建控制台: {console_response.status_code}")

if console_response.status_code in [200, 201]:
    console_data = console_response.json()
    console_id = console_data["id"]
    print(f"控制台 ID: {console_id}")
    
    time.sleep(2)
    
    print("\n发送命令...")
    send_command_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
    
    commands = [
        "cd /home/8210232126/django-cms-blog\n",
        "ls -la static/\n",
        "ls -la templates/\n",
        "source /home/8210232126/.virtualenvs/myvirtualenv/bin/activate\n",
        "python manage.py collectstatic --noinput\n",
        "ls -la staticfiles/\n",
        "echo '=== DONE ==='\n"
    ]
    
    for cmd in commands:
        requests.post(send_command_url, headers=headers, json={"input": cmd})
        time.sleep(2)
    
    print("等待 20 秒...")
    time.sleep(20)
    
    print("\n=== 步骤 3: 重载网站...\n")
    reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
    reload_response = requests.post(reload_url, headers=headers)
    print(f"重载: {reload_response.status_code}")
    
    print("\n" + "="*50)
    print("✅ 完成！")
    print(f"访问: https://{PA_USERNAME}.pythonanywhere.com/admin/")
    print("\n账号: admin")
    print("密码: admin123456")
    print("\n请等待 1 分钟后刷新页面！")
else:
    print(f"❌ 错误: {console_response.text}")
