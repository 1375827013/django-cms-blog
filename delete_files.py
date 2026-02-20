import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

files_to_delete = [
    f"/home/{PA_USERNAME}/django-cms-blog/app_name/management/commands/createadmin.py",
    f"/home/{PA_USERNAME}/django-cms-blog/app_name/management/commands/__init__.py",
    f"/home/{PA_USERNAME}/django-cms-blog/app_name/management/__init__.py",
    f"/home/{PA_USERNAME}/django-cms-blog/project_name/views.py",
]

print("删除冲突文件...")
for file_path in files_to_delete:
    url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/files/path{file_path}"
    response = requests.delete(url, headers=headers)
    print(f"  {file_path}: {response.status_code}")

print("\n✅ 文件已删除")
