# 网页资源文件夹 (web_assets)

这个文件夹包含所有与网页相关的文件：

## 目录结构
- `templates/` - Django 模板文件
  - `admin/` - 管理后台模板
  - `registration/` - 注册相关模板
- `static/` - 静态文件 (CSS, JS, 图片等)

## 管理后台美化
- `templates/admin/base_site.html` - 基础模板，包含紫色渐变样式
- `templates/admin/index.html` - 管理首页，卡片式布局
- `templates/admin/login.html` - 登录页面，渐变背景

## 配置说明
在 `settings.py` 中需要配置：
```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / "web_assets/templates"],
    },
]

STATICFILES_DIRS = [BASE_DIR / "web_assets/static"]
```
