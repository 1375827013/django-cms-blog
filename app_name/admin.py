from django.contrib import admin
from .models import Article
from .models import CalendarEvent

admin.site.register(Article)

@admin.register(CalendarEvent)  # 装饰器注册方式，更简洁
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'event_type', 'user')  # 列表显示项
    list_filter = ('event_type', 'date', 'user')  # 右侧过滤器
    search_fields = ('title', 'description')  # 搜索框
    date_hierarchy = 'date'  # 按日期层级导航（非常实用！）