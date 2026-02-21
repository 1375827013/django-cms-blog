# 高考志愿填报助手 - 项目结构说明

## 项目概述
这是一个基于 Django 的高考志愿填报助手网站，包含管理后台美化功能。

## 项目结构
```
高考志愿填报助手/
├── 📁 web_assets/           # 网页资源文件夹
│   ├── 📁 templates/        # 模板文件
│   │   ├── 📁 admin/        # 管理后台模板
│   │   │   ├── base_site.html  # 基础模板（紫色渐变样式）
│   │   │   ├── index.html      # 管理首页（卡片布局）
│   │   │   └── login.html      # 登录页面（渐变背景）
│   │   ├── 📁 registration/    # 注册相关模板
│   │   └── base.html           # 基础模板
│   └── 📁 static/           # 静态文件
│       └── 📁 css/          # CSS 样式文件
│           ├── admin_custom.css  # 管理后台自定义样式
│           └── style.css         # 通用样式
│
├── 📁 app_name/             # Django 应用
│   ├── admin.py            # 管理后台配置
│   ├── models.py           # 数据模型（学生、大学、专业等）
│   ├── views.py            # 视图函数
│   ├── urls.py             # URL 路由
│   ├── 📁 templates/       # 应用特定模板
│   └── 📁 migrations/      # 数据库迁移文件
│
├── 📁 project_name/         # 项目配置
│   ├── settings.py         # 配置文件
│   ├── urls.py             # 主 URL 配置
│   └── wsgi.py             # WSGI 配置
│
├── 📁 media/                # 用户上传文件
├── 📁 staticfiles/          # 收集的静态文件
├── db.sqlite3              # 数据库文件
├── manage.py               # Django 管理脚本
├── requirements.txt        # 依赖包列表
└── README.md              # 项目说明
```

## 文件分类说明

### 🎨 网页相关文件 (web_assets/)
- **模板文件**：所有 HTML 模板，包含管理后台美化
- **静态文件**：CSS、JS、图片等前端资源

### 🐍 Django 应用文件 (app_name/)
- **核心逻辑**：数据模型、视图函数、URL 路由
- **管理后台**：模型注册、自定义管理界面

### ⚙️ 项目配置 (project_name/)
- **设置文件**：数据库、模板、静态文件配置
- **URL 配置**：网站路由映射

### 📦 部署相关文件
- `pythonanywhere_mcp.py` - PythonAnywhere 部署脚本
- `trigger_deploy.py` - 触发部署脚本
- `create_admin.py` - 创建管理员脚本
- `init_data.py` - 初始化数据脚本

## 管理后台美化功能
- 紫色渐变头部导航栏
- 卡片式应用布局
- FontAwesome 图标集成
- 响应式设计

## 开发说明
- 使用 Django 5.2.10
- 支持中文本地化
- 适配 PythonAnywhere 部署
