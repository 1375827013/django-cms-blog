from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article  # 必须导入 Day 2 定义的模型

import calendar
from datetime import date
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import CalendarEvent

from django.contrib.auth.decorators import login_required

def article_list(request):
    # 1. 查询逻辑：使用 ORM 语法获取所有文章对象
    articles = Article.objects.all()
    
    # 2. 返回结果：将数据封装在字典中，交给对应的 HTML 模板
    return render(request, 'app_name/list.html', {'articles': articles})

def article_create(request):
    # 判断用户是否提交了数据
    if request.method == "POST":
        # 将文字数据(POST)和文件数据(FILES)一并交给表单类处理
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # 进阶操作：将文章与当前登录的用户绑定
            article = form.save(commit=False)
            article.author = request.user 
            article.save()
            return redirect('article_list')
            # 去掉原本的form.save()
    else:
        form = ArticleForm() # 如果是正常访问，给用户一个空表单
    
    return render(request, 'app_name/article_form.html', {'form': form})


    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # 进阶操作：将文章与当前登录的用户绑定
            article = form.save(commit=False)
            article.author = request.user 
            article.save()
            return redirect('article_list')
    # ...

@login_required
def calendar_view(request, year=None, month=None):
    """显示指定年月的日历，并标记有事件的日期"""
    # 获取当前年月，或使用传入的参数
    today = date.today()
    current_year = year if year else today.year
    current_month = month if month else today.month

    # 生成指定年月的日历矩阵
    cal = calendar.monthcalendar(current_year, current_month)
    month_name = calendar.month_name[current_month]

    # 查询这个月所有的当前用户的事件
    events = CalendarEvent.objects.filter(
        user=request.user,  # 只显示当前用户的事件
        date__year=current_year,
        date__month=current_month
    )

    # 创建一个字典，键为日期（天），值为当天的事件列表
    event_dict = {}
    for event in events:
        day = event.date.day
        if day not in event_dict:
            event_dict[day] = []
        # 安全地处理HTML，在模板中显示
        event_info = f'<div class="event-tag {event.event_type}">{event.title}</div>'
        event_dict[day].append(mark_safe(event_info))

    # 准备日历数据，将事件信息嵌入
    calendar_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append({'day': '', 'events': []})
            else:
                week_data.append({
                    'day': day,
                    'events': event_dict.get(day, []),
                    'is_today': (day == today.day and current_month == today.month and current_year == today.year)
                })
        calendar_data.append(week_data)

    # 计算上个月和下个月
    prev_month = current_month - 1 if current_month > 1 else 12
    prev_year = current_year if current_month > 1 else current_year - 1
    next_month = current_month + 1 if current_month < 12 else 1
    next_year = current_year if current_month < 12 else current_year + 1

    context = {
        'calendar_data': calendar_data,
        'month_name': month_name,
        'year': current_year,
        'month': current_month,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
        'today': today,
    }
    return render(request, 'app_name/calendar.html', context)