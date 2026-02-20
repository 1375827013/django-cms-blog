import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

base_project_path = f"/home/{PA_USERNAME}/django-cms-blog"

def create_file(path, content):
    url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/files/path{path}"
    files = {'content': ('file', content)}
    response = requests.post(url, headers=headers, files=files)
    return response

print("开始上传 Admin 美化文件...\n")

# 1. 上传 admin_custom.css
print("1. 上传 static/css/admin_custom.css...")
with open("static/css/admin_custom.css", "r", encoding="utf-8") as f:
    css_content = f.read()
r1 = create_file(f"{base_project_path}/static/css/admin_custom.css", css_content)
print(f"   状态码: {r1.status_code}")

# 2. 上传 base_site.html
print("\n2. 上传 templates/admin/base_site.html...")
with open("templates/admin/base_site.html", "r", encoding="utf-8") as f:
    base_content = f.read()
r2 = create_file(f"{base_project_path}/templates/admin/base_site.html", base_content)
print(f"   状态码: {r2.status_code}")

# 3. 上传 index.html
print("\n3. 上传 templates/admin/index.html...")
with open("templates/admin/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()
r3 = create_file(f"{base_project_path}/templates/admin/index.html", index_content)
print(f"   状态码: {r3.status_code}")

print("\n" + "="*50)
if r1.status_code in [200, 201] and r2.status_code in [200, 201] and r3.status_code in [200, 201]:
    print("✅ 文件上传成功！")
else:
    print("⚠️  部分文件上传完成")
print("\n现在触发网站重载...")

# 重载网站
reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
reload_response = requests.post(reload_url, headers=headers)
print(f"重载状态码: {reload_response.status_code}")

print("\n" + "="*50)
print("🎉 部署完成！")
print(f"访问地址: https://{PA_USERNAME}.pythonanywhere.com/admin/")
print("账号: admin")
print("密码: admin123456")
