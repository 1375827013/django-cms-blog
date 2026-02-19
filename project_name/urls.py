from django.contrib import admin
from django.urls import path, include  # 必须引入 include 模块

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView  # 新增导入

from django.views.generic import RedirectView  # 新增导入

urlpatterns = [
    # 空路径：重定向到文章列表
    path('', RedirectView.as_view(url='app_name/', permanent=False)),

    # 临时添加小火箭页面，放在最前面
    path('rocket/', TemplateView.as_view(template_name='default_index.html'), name='rocket'),

    # 管理后台
    path('admin/', admin.site.urls),

    # 应用路由入口：将所有以 app_name/ 开头的请求，转发给 app_name 应用自己的 urls.py 去处理。
    path('app_name/', include('app_name.urls')),
    
    # 认证路由：提供用户登录、登出、密码管理等标准认证功能页面。
    path('accounts/', include('django.contrib.auth.urls')),
]


# 逻辑：只在开发模式下，让 Django 能够根据 URL 找到 media 文件夹里的图片
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)