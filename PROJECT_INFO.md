# Django + Streamlit + Supabase 考研数据查询系统

## 项目概述

这是一个结合 Django 后台管理和 Streamlit 前端展示的考研数据查询系统，数据存储在 Supabase (PostgreSQL) 数据库中。

## 部署信息

### GitHub 仓库
- 地址: https://github.com/1375827013/django-cms-blog
- 用户名: 1375827013

### PythonAnywhere
- 账户: 8210232126
- 域名: https://8210232126.pythonanywhere.com

## 技术栈

- **后端**: Django 5.2.10
- **前端**: Streamlit 1.40.0
- **数据库**: Supabase (PostgreSQL)
- **ORM**: psycopg2-binary 2.9.9
- **其他**: python-dotenv, pillow

## 数据库配置

Supabase 连接信息 (已配置在 settings.py):
```
HOST: db.xgwgtlealmcynvizozfd.supabase.co
PORT: 5432
NAME: postgres
USER: postgres
```

### Supabase 表结构

1. **schools** (考研院校表)
   - dm: 院校代码 (主键)
   - mc: 院校名称
   - province_code: 省份代码
   - href: 相关链接

2. **provinces** (省份表)
   - code: 省份代码 (主键)
   - name: 省份名称

3. **categories** (专业类别表)
   - dm: 类别代码
   - mc: 类别名称

## 项目结构

```
project_name/
├── src/
│   ├── app_name/              # Django 应用
│   │   ├── models.py          # 数据模型 (含 KaoyanSchool, KaoyanProvince)
│   │   ├── views.py          # 视图函数
│   │   ├── urls.py           # URL 路由
│   │   ├── admin.py          # Django 管理后台
│   │   └── templates/        # HTML 模板
│   ├── project_name/          # Django 项目配置
│   │   ├── settings.py       # 数据库和 Supabase 配置
│   │   ├── urls.py           # 主 URL 配置
│   │   └── views.py          # 项目视图
│   ├── streamlit_app.py      # Streamlit 前端应用
│   ├── requirements.txt      # Python 依赖
│   └── manage.py             # Django 管理脚本
└── .env                      # 环境变量 (不在 GitHub 中)
```

## 关键文件说明

### 1. Django 模型 (app_name/models.py)

```python
# 考研院校模型 - 映射到 Supabase 的 schools 表
class KaoyanSchool(models.Model):
    dm = models.CharField('院校代码', max_length=20, unique=True)
    mc = models.CharField('院校名称', max_length=100)
    province_code = models.CharField('省份代码', max_length=10, blank=True)
    href = models.TextField('链接', blank=True)
    
    class Meta:
        db_table = 'schools'
        managed = False  # 不创建表，只读取现有表

# 省份模型 - 映射到 Supabase 的 provinces 表
class KaoyanProvince(models.Model):
    code = models.CharField('省份代码', max_length=10, unique=True)
    name = models.CharField('省份名称', max_length=50)
    
    class Meta:
        db_table = 'provinces'
        managed = False
```

### 2. Django 配置 (project_name/settings.py)

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": os.getenv('DB_PASSWORD', ''),
        "HOST": "db.xgwgtlealmcynvizozfd.supabase.co",
        "PORT": "5432",
    }
}

ALLOWED_HOSTS = ['8210232126.pythonanywhere.com', 'localhost', '127.0.0.1']
```

### 3. Streamlit 应用 (streamlit_app.py)

- 连接 Supabase 获取数据
- 按省份分组显示院校
- 提供搜索功能
- 一键展开/收纳功能
- 使用 @st.cache_resource 缓存 Supabase 客户端

## 功能列表

### Django 后台
- 考研院校列表 (/kaoyan/schools/)
- 院校详情页 (/kaoyan/schools/<dm>/)
- 专业类别列表 (/kaoyan/categories/)
- Django 管理后台 (/admin/)

### Streamlit 前端
- 按省份查院校
- 搜索院校
- 专业类别展示

## 环境变量

需要在 .env 文件中配置:
```
SUPABASE_URL=https://xgwgtlealmcynvizozfd.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
DB_PASSWORD=adsefvsw234sfe
```

## 运行命令

### Django
```bash
cd src
python manage.py runserver
```

### Streamlit
```bash
cd src
streamlit run streamlit_app.py --server.port 8501
```

### PythonAnywhere 部署
1. 从 GitHub 拉取代码
2. 安装依赖: pip install -r requirements.txt
3. 配置 .env 文件
4. 在 PythonAnywhere Web 标签页配置 WSGI

## 注意事项

1. .env 和 streamlit.env 文件不在 GitHub 中，需要手动配置
2. Django 模型使用 managed=False，因为表已在 Supabase 中存在
3. Streamlit 使用 @st.cache_resource 而非 @st.cache_data 缓存 Supabase 客户端
