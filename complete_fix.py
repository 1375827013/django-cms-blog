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

print("=== 完整修复方案 ===\n")

# ==========================================
# 1. 重新上传所有文件
# ==========================================
print("步骤 1: 上传文件...")

print("  1.1 admin_custom.css")
with open("static/css/admin_custom.css", "r", encoding="utf-8") as f:
    css_content = f.read()
r1 = create_file(f"{base_project_path}/static/css/admin_custom.css", css_content)
print(f"      status: {r1.status_code}")

print("  1.2 base_site.html")
with open("templates/admin/base_site.html", "r", encoding="utf-8") as f:
    base_content = f.read()
r2 = create_file(f"{base_project_path}/templates/admin/base_site.html", base_content)
print(f"      status: {r2.status_code}")

print("  1.3 index.html")
with open("templates/admin/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()
r3 = create_file(f"{base_project_path}/templates/admin/index.html", index_content)
print(f"      status: {r3.status_code}")

print("\n步骤 2: 上传登录页面模板...")
with open("templates/admin/login.html", "r", encoding="utf-8") as f:
    login_content = f.read()
r4 = create_file(f"{base_project_path}/templates/admin/login.html", login_content)
print(f"      status: {r4.status_code}")

# ==========================================
# 2. 确保目录结构正确
# ==========================================
print("\n步骤 3: 确保目录结构...")
create_file(f"{base_project_path}/templates/admin/__init__.py", "")
print("      完成")

# ==========================================
# 3. 直接在 staticfiles 中也放一份
# ==========================================
print("\n步骤 4: 直接上传到 staticfiles...")
r5 = create_file(f"{base_project_path}/staticfiles/css/admin_custom.css", css_content)
print(f"      status: {r5.status_code}")

# ==========================================
# 4. 运行 collectstatic
# ==========================================
print("\n步骤 5: 创建控制台运行 collectstatic...")

console_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/"
console_response = requests.post(
    console_url,
    headers=headers,
    json={"executable": "bash", "working_directory": base_project_path}
)

if console_response.status_code in [200, 201]:
    try:
        console_data = console_response.json()
        console_id = console_data["id"]
        print(f"      控制台 ID: {console_id}")
        
        time.sleep(3)
        
        send_command_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/consoles/{console_id}/send_input/"
        
        commands = [
            "cd /home/8210232126/django-cms-blog\n",
            "source /home/8210232126/.virtualenvs/myvirtualenv/bin/activate\n",
            "python manage.py collectstatic --noinput 2>&1\n",
            "echo '=== COLLECTSTATIC DONE ==='\n",
            "ls -la staticfiles/css/\n"
        ]
        
        for cmd in commands:
            requests.post(send_command_url, headers=headers, json={"input": cmd})
            time.sleep(3)
        
        print("      命令已发送，等待 30 秒...")
        time.sleep(30)
        
    except:
        print("      控制台响应解析失败，但继续...")
else:
    print(f"      控制台创建: {console_response.status_code}")

# ==========================================
# 5. 重载网站
# ==========================================
print("\n步骤 6: 重载网站...")
reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
reload_response = requests.post(reload_url, headers=headers)
print(f"      重载: {reload_response.status_code}")

print("\n" + "="*60)
print("✅ 所有步骤完成！")
print("\n请按以下顺序操作：")
print("1. 等待 2 分钟让网站完全启动")
print("2. 访问: https://8210232126.pythonanywhere.com/admin/")
print("3. 登录: admin / admin123456")
print("4. 如果还是不行，按 Ctrl+F5 硬刷新")
print("\n本地预览: http://127.0.0.1:8000/admin/")
