import requests
import time

PA_USERNAME = "8210232126"
PA_API_TOKEN = "f06aaa35de2008e9cb167d193c76fb607cb2cc59"
headers = {"Authorization": f"Token {PA_API_TOKEN}"}

print("1. 先检查静态文件是否存在...")
check_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/files/path/home/{PA_USERNAME}/django-cms-blog/static/css/admin_custom.css"
check_r = requests.get(check_url, headers=headers)
print(f"   文件存在: {check_r.status_code}")

print("\n2. 重载网站...")
reload_url = f"https://www.pythonanywhere.com/api/v0/user/{PA_USERNAME}/webapps/{PA_USERNAME}.pythonanywhere.com/reload/"
reload_r = requests.post(reload_url, headers=headers)
print(f"   重载状态: {reload_r.status_code}")

print("\n" + "="*50)
print("✅ 完成！")
print("\n请在浏览器中：")
print("1. 访问 https://8210232126.pythonanywhere.com/admin/")
print("2. 登录账号: admin")
print("3. 登录密码: admin123456")
print("\n如果样式还没显示，请等待 30 秒后：")
print("   - 按 Ctrl+F5（Windows）或 Cmd+Shift+R（Mac）硬刷新")
print("   - 或者清除浏览器缓存后刷新")
