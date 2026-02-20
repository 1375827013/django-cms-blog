import requests

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

base_path = f"/home/{PA_USERNAME}/django-cms-blog/app_name/management"
commands_path = f"{base_path}/commands"

init_content = ""
createadmin_content = '''from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = '创建或重置管理员账号'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = 'admin'
        password = 'admin123456'
        email = 'admin@example.com'
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'管理员密码已重置'))
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'管理员账号已创建'))
        
        self.stdout.write(f'用户名: {username}')
        self.stdout.write(f'密码: {password}')
'''

def create_file(path, content):
    url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/files/path{path}"
    files = {'content': ('file', content)}
    response = requests.post(url, headers=headers, files=files)
    return response

print("创建目录结构...")

r1 = create_file(f"{base_path}/__init__.py", init_content)
print(f"  management/__init__.py: {r1.status_code}")

r2 = create_file(f"{commands_path}/__init__.py", init_content)
print(f"  commands/__init__.py: {r2.status_code}")

r3 = create_file(f"{commands_path}/createadmin.py", createadmin_content)
print(f"  createadmin.py: {r3.status_code}")

if r3.status_code in [200, 201]:
    print("\n✅ 文件创建成功!")
else:
    print(f"\n响应: {r3.text[:200]}")
