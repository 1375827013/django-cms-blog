#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
password = 'admin123456'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ 管理员账号创建成功！")
    print(f"用户名: {username}")
    print(f"密码: {password}")
    print(f"邮箱: {email}")
else:
    print(f"❌ 用户名 '{username}' 已存在")
    existing_user = User.objects.get(username=username)
    print(f"如需重置密码，请运行:")
    print(f"python manage.py changepassword {username}")
