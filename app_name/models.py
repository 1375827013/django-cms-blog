from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField('姓名', max_length=50)
    province = models.CharField('省份', max_length=20)
    total_score = models.IntegerField('总分', help_text='高考总分')
    chinese_score = models.IntegerField('语文', null=True, blank=True)
    math_score = models.IntegerField('数学', null=True, blank=True)
    english_score = models.IntegerField('英语', null=True, blank=True)
    comprehensive_score = models.IntegerField('综合', null=True, blank=True)
    subject_type = models.CharField('科类', max_length=10, choices=[('理科', '理科'), ('文科', '文科')], default='理科')
    year = models.IntegerField('高考年份', default=2024)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '学生档案'
        verbose_name_plural = '学生档案'

    def __str__(self):
        return f"{self.name} - {self.total_score}分"

class University(models.Model):
    name = models.CharField('大学名称', max_length=100, unique=True)
    province = models.CharField('所在省份', max_length=20)
    city = models.CharField('所在城市', max_length=20, blank=True)
    university_type = models.CharField('办学类型', max_length=20, choices=[
        ('985', '985工程'),
        ('211', '211工程'),
        ('双一流', '双一流'),
        ('普通本科', '普通本科'),
        ('专科', '专科'),
    ], default='普通本科')
    level = models.CharField('办学层次', max_length=20, choices=[
        ('本科', '本科'),
        ('专科', '专科'),
    ], default='本科')
    ranking = models.IntegerField('全国排名', null=True, blank=True, help_text='软科排名')
    description = models.TextField('学校简介', blank=True)
    website = models.URLField('官网', blank=True)
    logo = models.ImageField('校徽', upload_to='university_logos/', blank=True, null=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '大学信息'
        verbose_name_plural = '大学信息'
        ordering = ['ranking']

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField('专业名称', max_length=100, unique=True)
    category = models.CharField('专业类别', max_length=50, choices=[
        ('工学', '工学'),
        ('理学', '理学'),
        ('文学', '文学'),
        ('历史学', '历史学'),
        ('哲学', '哲学'),
        ('经济学', '经济学'),
        ('管理学', '管理学'),
        ('法学', '法学'),
        ('教育学', '教育学'),
        ('艺术学', '艺术学'),
        ('医学', '医学'),
        ('农学', '农学'),
    ])
    code = models.CharField('专业代码', max_length=10, unique=True)
    description = models.TextField('专业介绍', blank=True)
    employment_rate = models.DecimalField('就业率', max_digits=5, decimal_places=2, null=True, blank=True, help_text='百分比')
    salary_range = models.CharField('薪资范围', max_length=50, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '专业信息'
        verbose_name_plural = '专业信息'
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"

class AdmissionScore(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name='大学')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True, verbose_name='专业')
    province = models.CharField('招生省份', max_length=20)
    subject_type = models.CharField('科类', max_length=10, choices=[('理科', '理科'), ('文科', '文科')])
    year = models.IntegerField('年份')
    min_score = models.IntegerField('最低投档分')
    avg_score = models.IntegerField('平均分', null=True, blank=True)
    max_score = models.IntegerField('最高分', null=True, blank=True)
    ranking = models.IntegerField('最低位次', null=True, blank=True, help_text='全省排名')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '录取分数线'
        verbose_name_plural = '录取分数线'
        ordering = ['-year', '-min_score']

    def __str__(self):
        return f"{self.university.name} {self.year}年 {self.min_score}分"

class CollegePreference(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, verbose_name='学生')
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name='大学')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True, verbose_name='专业')
    preference_order = models.IntegerField('志愿顺序', help_text='1-6，1为第一志愿')
    is_adjusted = models.BooleanField('是否服从调剂', default=False)
    notes = models.TextField('备注', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '志愿填报'
        verbose_name_plural = '志愿填报'
        ordering = ['preference_order']

    def __str__(self):
        return f"第{self.preference_order}志愿: {self.university.name}"
