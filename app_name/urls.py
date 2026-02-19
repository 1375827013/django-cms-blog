
from django.urls import path
from . import views

urlpatterns = [
    # 新增：处理 /app_name/ 的首页路由
    path('', views.article_list, name='index'),

    # 逻辑：当用户访问域名/app_name/list/ 时，调用视图函数 article_list
    path('list/', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),

    # 日历视图（支持带年月参数和不带参数）
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar_view'),
]