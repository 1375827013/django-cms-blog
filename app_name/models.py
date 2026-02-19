from django.db import models
from django.contrib.auth.models import User  # 关联用户
from django.urls import reverse

class Article(models.Model):
    # 定义表字段：标题、内容、创建时间
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    created = models.DateTimeField('创建时间', auto_now_add=True)
    image = models.ImageField('封面图', upload_to='article_covers/', blank=True, null=True)
    
    class Meta: 
        verbose_name = '文章' 
        verbose_name_plural = '文章列表' 
        ordering = ['-created'] # 按创建时间倒序排列

    def __str__(self):
        return self.title
    


class CalendarEvent(models.Model):
    # 事件基本字段
    title = models.CharField('标题', max_length=200)
    description = models.TextField('描述', blank=True)
    date = models.DateField('日期')  # 事件发生的日期
    start_time = models.TimeField('开始时间', blank=True, null=True)  # 可选
    end_time = models.TimeField('结束时间', blank=True, null=True)  # 可选
    
    # 事件分类（如：作业、考试、复习、个人）
    EVENT_TYPE_CHOICES = [
        ('homework', '作业'),
        ('exam', '考试'),
        ('review', '复习'),
        ('personal', '个人事务'),
        ('other', '其他'),
    ]
    event_type = models.CharField('类型', max_length=20, choices=EVENT_TYPE_CHOICES, default='homework')
    
    # 关联到用户（重要：这样每个人只能看到自己的事件）
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 自动记录创建时间
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.title}"

    def get_absolute_url(self):
        """告诉Django创建/更新后跳转到哪里，对Admin友好"""
        return reverse('calendar_view')  # 我们稍后会创建这个视图名

    class Meta:
        ordering = ['date', 'start_time']  # 默认按日期、时间排序
        verbose_name = '日历事件'
        verbose_name_plural = '日历事件'