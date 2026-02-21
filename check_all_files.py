import os

print("=== 检查所有关键文件是否完整 ===")

# Django 项目结构检查
required_dirs = [
    "project_name",
    "app_name", 
    "templates",
    "templates/admin",
    "static"
]

print("\n1. 检查目录结构")
for dir_path in required_dirs:
    if os.path.exists(dir_path):
        print(f"✓ {dir_path}/")
    else:
        print(f"✗ {dir_path}/ 不存在")

# 关键文件检查
required_files = [
    "project_name/settings.py",
    "project_name/urls.py", 
    "project_name/wsgi.py",
    "app_name/admin.py",
    "app_name/models.py",
    "app_name/views.py",
    "templates/admin/base_site.html",
    "templates/admin/index.html",
    "templates/admin/login.html",
    "manage.py",
    "requirements.txt"
]

print("\n2. 检查关键文件")
for file_path in required_files:
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"✓ {file_path} - {size} 字节")
    else:
        print(f"✗ {file_path} 不存在")

# 检查模板内容
print("\n3. 检查模板内容")
with open("templates/admin/base_site.html", "r", encoding="utf-8") as f:
    base_site_content = f.read()
    if '高考志愿填报助手' in base_site_content:
        print("✓ base_site.html 包含标题")
    if 'linear-gradient' in base_site_content:
        print("✓ base_site.html 包含渐变样式")

with open("templates/admin/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()
    if 'app-dashboard' in index_content:
        print("✓ index.html 包含卡片布局")

with open("templates/admin/login.html", "r", encoding="utf-8") as f:
    login_content = f.read()
    if '高考志愿填报助手' in login_content:
        print("✓ login.html 包含标题")

# 检查 settings.py 配置
print("\n4. 检查 settings.py 配置")
with open("project_name/settings.py", "r", encoding="utf-8") as f:
    settings_content = f.read()
    if 'DIRS: [BASE_DIR / "templates"]' in settings_content:
        print("✓ TEMPLATES DIRS 配置正确")
    if '"app_name"' in settings_content:
        print("✓ app_name 在 INSTALLED_APPS 中")

# 检查 admin.py 模型注册
print("\n5. 检查 admin.py 模型注册")
with open("app_name/admin.py", "r", encoding="utf-8") as f:
    admin_content = f.read()
    if 'admin.site.register' in admin_content:
        print("✓ admin.py 包含模型注册")
    if 'StudentProfile' in admin_content:
        print("✓ 包含 StudentProfile 模型")
    if 'University' in admin_content:
        print("✓ 包含 University 模型")

print("\n✅ 所有关键文件检查完成！")
