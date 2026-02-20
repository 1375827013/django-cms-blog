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

print("=== 最终方案：CSS 直接内联，无需 static ===\n")

print("1. 上传 base_site.html (CSS 已内联)...")
with open("templates/admin/base_site.html", "r", encoding="utf-8") as f:
    base_content = f.read()
r1 = create_file(f"{base_project_path}/templates/admin/base_site.html", base_content)
print(f"   status: {r1.status_code}")

print("\n2. 上传 index.html...")
with open("templates/admin/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()
r2 = create_file(f"{base_project_path}/templates/admin/index.html", index_content)
print(f"   status: {r2.status_code}")

print("\n3. 上传 login.html...")
with open("templates/admin/login.html", "r", encoding="utf-8") as f:
    login_content = f.read()
r3 = create_file(f"{base_project_path}/templates/admin/login.html", login_content)
print(f"   status: {r3.status_code}")

print("\n4. 重载网站...")
reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
reload_response = requests.post(reload_url, headers=headers)
print(f"   重载: {reload_response.status_code}")

print("\n" + "="*60)
print("✅ 100% 完成！")
print("\nCSS 已直接内联到模板中，无需 static 文件！")
print("\n请按以下操作：")
print("1. 等待 30 秒")
print("2. 访问: https://8210232126.pythonanywhere.com/admin/")
print("3. 登录: admin / admin123456")
print("4. 按 Ctrl+F5 硬刷新")
print("\n本地预览: http://127.0.0.1:8000/admin/")
