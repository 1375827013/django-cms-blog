#!/usr/bin/env python3
"""
初始化高考志愿填报助手的数据
"""

import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
django.setup()

from app_name.models import University, Major, AdmissionScore

def init_universities():
    """初始化大学数据"""
    universities = [
        {
            'name': '清华大学',
            'province': '北京',
            'city': '北京',
            'university_type': '985',
            'level': '本科',
            'ranking': 1,
            'website': 'https://www.tsinghua.edu.cn',
            'description': '中国顶尖的综合性大学'
        },
        {
            'name': '北京大学',
            'province': '北京',
            'city': '北京',
            'university_type': '985',
            'level': '本科',
            'ranking': 2,
            'website': 'https://www.pku.edu.cn',
            'description': '历史悠久的综合性大学'
        },
        {
            'name': '浙江大学',
            'province': '浙江',
            'city': '杭州',
            'university_type': '985',
            'level': '本科',
            'ranking': 3,
            'website': 'https://www.zju.edu.cn',
            'description': '综合实力强劲的大学'
        },
        {
            'name': '复旦大学',
            'province': '上海',
            'city': '上海',
            'university_type': '985',
            'level': '本科',
            'ranking': 4,
            'website': 'https://www.fudan.edu.cn',
            'description': '人文社科领域的强校'
        },
        {
            'name': '上海交通大学',
            'province': '上海',
            'city': '上海',
            'university_type': '985',
            'level': '本科',
            'ranking': 5,
            'website': 'https://www.sjtu.edu.cn',
            'description': '理工科强校'
        },
        {
            'name': '南京大学',
            'province': '江苏',
            'city': '南京',
            'university_type': '985',
            'level': '本科',
            'ranking': 6,
            'website': 'https://www.nju.edu.cn',
            'description': '综合实力强校'
        },
        {
            'name': '中山大学',
            'province': '广东',
            'city': '广州',
            'university_type': '985',
            'level': '本科',
            'ranking': 14,
            'website': 'https://www.sysu.edu.cn',
            'description': '华南地区强校'
        },
        {
            'name': '华南理工大学',
            'province': '广东',
            'city': '广州',
            'university_type': '985',
            'level': '本科',
            'ranking': 25,
            'website': 'https://www.scut.edu.cn',
            'description': '理工科强校'
        },
    ]

    for uni_data in universities:
        uni, created = University.objects.get_or_create(
            name=uni_data['name'],
            defaults=uni_data
        )
        if created:
            print(f'创建大学: {uni.name}')
        else:
            print(f'大学已存在: {uni.name}')

def init_majors():
    """初始化专业数据"""
    majors = [
        {'name': '计算机科学与技术', 'code': '080901', 'category': '工学', 'employment_rate': 95, 'salary_range': '15-30万/年', 'description': '计算机科学与技术专业培养具有良好科学素养，系统地掌握计算机科学与技术的基本理论、基本知识、基本技能和方法的高级专门人才。'},
        {'name': '软件工程', 'code': '080902', 'category': '工学', 'employment_rate': 96, 'salary_range': '16-35万/年', 'description': '软件工程专业培养掌握软件工程专业知识和技能，能够从事软件设计、开发、测试、维护等工作的高级工程技术人才。'},
        {'name': '人工智能', 'code': '080717T', 'category': '工学', 'employment_rate': 97, 'salary_range': '20-40万/年', 'description': '人工智能专业培养掌握人工智能基础理论、方法和技术的高素质复合型人才。'},
        {'name': '数据科学与大数据技术', 'code': '080910T', 'category': '工学', 'employment_rate': 94, 'salary_range': '18-35万/年', 'description': '数据科学与大数据技术专业培养具有数据科学素养，掌握大数据处理与分析能力的专门人才。'},
        {'name': '电子信息工程', 'code': '080701', 'category': '工学', 'employment_rate': 93, 'salary_range': '12-25万/年', 'description': '电子信息工程专业培养具有电子技术和信息系统基础知识的高级工程技术人才。'},
        {'name': '机械工程', 'code': '080201', 'category': '工学', 'employment_rate': 92, 'salary_range': '10-20万/年', 'description': '机械工程专业培养从事机械设计制造及自动化、机电一体化等工作的高级工程技术人才。'},
        {'name': '临床医学', 'code': '100201K', 'category': '医学', 'employment_rate': 90, 'salary_range': '15-40万/年', 'description': '临床医学专业培养掌握基础医学、临床医学的基础理论、基本知识和医疗技能的医学专门人才。'},
        {'name': '金融学', 'code': '020301K', 'category': '经济学', 'employment_rate': 92, 'salary_range': '15-50万/年', 'description': '金融学专业培养具有全球视野、创新精神和实践能力的金融专业人才。'},
        {'name': '会计学', 'code': '120203K', 'category': '管理学', 'employment_rate': 94, 'salary_range': '10-25万/年', 'description': '会计学专业培养掌握会计、审计、财务管理等知识的高级专门人才。'},
        {'name': '法学', 'code': '030101K', 'category': '法学', 'employment_rate': 88, 'salary_range': '10-30万/年', 'description': '法学专业培养系统掌握法学知识，熟悉我国法律的高级专门人才。'},
        {'name': '汉语言文学', 'code': '050101', 'category': '文学', 'employment_rate': 89, 'salary_range': '8-20万/年', 'description': '汉语言文学专业培养具有汉语言文学基本理论、基础知识和基本技能的高级专门人才。'},
        {'name': '数学与应用数学', 'code': '070101', 'category': '理学', 'employment_rate': 91, 'salary_range': '12-30万/年', 'description': '数学与应用数学专业培养掌握数学科学的基本理论与基本方法的高级专门人才。'},
        {'name': '物理学', 'code': '070201', 'category': '理学', 'employment_rate': 90, 'salary_range': '10-28万/年', 'description': '物理学专业培养掌握物理学的基本理论与方法的高级专门人才。'},
        {'name': '生物学', 'code': '071001', 'category': '理学', 'employment_rate': 89, 'salary_range': '10-25万/年', 'description': '生物学专业培养掌握生物学基础理论、基本知识和实验技能的高级专门人才。'},
    ]

    for major_data in majors:
        major, created = Major.objects.get_or_create(
            name=major_data['name'],
            defaults=major_data
        )
        if created:
            print(f'创建专业: {major.name}')
        else:
            print(f'专业已存在: {major.name}')

def init_admission_scores():
    """初始化录取分数线数据"""
    universities = University.objects.all()[:5]
    provinces = ['北京', '上海', '广东', '江苏', '浙江']
    subject_types = ['理科', '文科']
    years = [2023, 2022, 2021]

    for university in universities:
        for province in provinces:
            for subject_type in subject_types:
                for year in years:
                    base_score = 650 if university.ranking <= 3 else 600
                    min_score = base_score - university.ranking * 2
                    avg_score = min_score + 10
                    max_score = min_score + 30
                    
                    AdmissionScore.objects.get_or_create(
                        university=university,
                        province=province,
                        subject_type=subject_type,
                        year=year,
                        defaults={
                            'min_score': min_score,
                            'avg_score': avg_score,
                            'max_score': max_score,
                        }
                    )
    print('录取分数线初始化完成')

if __name__ == '__main__':
    print('开始初始化数据...')
    init_universities()
    init_majors()
    init_admission_scores()
    print('数据初始化完成！')
