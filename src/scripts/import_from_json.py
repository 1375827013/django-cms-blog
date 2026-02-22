# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'

import django
django.setup()

from app_name.models import University

UNIVERSITIES_985 = [
    {"name": "清华大学", "province": "北京", "city": "北京", "ranking": 1, "website": "https://www.tsinghua.edu.cn/", "description": "清华大学是中国著名高等学府，坐落于北京西北郊风景秀丽的清华园，是中国高层次人才培养和科学技术研究的重要基地。"},
    {"name": "北京大学", "province": "北京", "city": "北京", "ranking": 2, "website": "https://www.pku.edu.cn/", "description": "北京大学创办于1898年，初名京师大学堂，是中国第一所国立综合性大学，也是当时中国最高教育行政机关。"},
    {"name": "浙江大学", "province": "浙江", "city": "杭州", "ranking": 3, "website": "https://www.zju.edu.cn/", "description": "浙江大学是一所历史悠久、声誉卓著的高等学府，坐落于中国历史文化名城、风景旅游胜地杭州。"},
    {"name": "上海交通大学", "province": "上海", "city": "上海", "ranking": 4, "website": "https://www.sjtu.edu.cn/", "description": "上海交通大学是我国历史最悠久、享誉海内外的著名高等学府之一，是教育部直属并与上海市共建的全国重点大学。"},
    {"name": "复旦大学", "province": "上海", "city": "上海", "ranking": 5, "website": "https://www.fudan.edu.cn/", "description": "复旦大学创建于1905年，原名复旦公学，是中国人自主创办的第一所高等院校。"},
    {"name": "南京大学", "province": "江苏", "city": "南京", "ranking": 6, "website": "https://www.nju.edu.cn/", "description": "南京大学是一所源远流长的高等学府，近代校史肇始于1902年创建的三江师范学堂。"},
    {"name": "中国科学技术大学", "province": "安徽", "city": "合肥", "ranking": 7, "website": "https://www.ustc.edu.cn/", "description": "中国科学技术大学是中国科学院所属的一所以前沿科学和高新技术为主的综合性全国重点大学。"},
    {"name": "华中科技大学", "province": "湖北", "city": "武汉", "ranking": 8, "website": "https://www.hust.edu.cn/", "description": "华中科技大学是国家教育部直属重点综合性大学，由原华中理工大学、同济医科大学、武汉城市建设学院于2000年合并成立。"},
    {"name": "武汉大学", "province": "湖北", "city": "武汉", "ranking": 9, "website": "https://www.whu.edu.cn/", "description": "武汉大学是国家教育部直属重点综合性大学，是国家985工程和211工程重点建设高校。"},
    {"name": "西安交通大学", "province": "陕西", "city": "西安", "ranking": 10, "website": "https://www.xjtu.edu.cn/", "description": "西安交通大学是国家教育部直属重点大学，为我国最早兴办的高等学府之一。"},
    {"name": "中山大学", "province": "广东", "city": "广州", "ranking": 11, "website": "https://www.sysu.edu.cn/", "description": "中山大学由孙中山先生创办，有着一百多年办学传统，是中国南方科学研究、文化学术与人才培养的重镇。"},
    {"name": "哈尔滨工业大学", "province": "黑龙江", "city": "哈尔滨", "ranking": 12, "website": "https://www.hit.edu.cn/", "description": "哈尔滨工业大学隶属于工业和信息化部，是首批进入国家211工程和985工程建设的高校。"},
    {"name": "北京航空航天大学", "province": "北京", "city": "北京", "ranking": 13, "website": "https://www.buaa.edu.cn/", "description": "北京航空航天大学创建于1952年，是新中国第一所航空航天高等学府。"},
    {"name": "同济大学", "province": "上海", "city": "上海", "ranking": 14, "website": "https://www.tongji.edu.cn/", "description": "同济大学历史悠久、声誉卓著，是中国最早的国立大学之一。"},
    {"name": "四川大学", "province": "四川", "city": "成都", "ranking": 15, "website": "https://www.scu.edu.cn/", "description": "四川大学是教育部直属全国重点大学，是国家布局在中国西部的重点建设的高水平研究型综合大学。"},
    {"name": "东南大学", "province": "江苏", "city": "南京", "ranking": 16, "website": "https://www.seu.edu.cn/", "description": "东南大学坐落于六朝古都南京，是享誉海内外的著名高等学府。"},
    {"name": "北京理工大学", "province": "北京", "city": "北京", "ranking": 17, "website": "https://www.bit.edu.cn/", "description": "北京理工大学1940年诞生于延安，是中国共产党创办的第一所理工科大学。"},
    {"name": "南开大学", "province": "天津", "city": "天津", "ranking": 18, "website": "https://www.nankai.edu.cn/", "description": "南开大学是教育部直属重点综合性大学，是敬爱的周恩来总理的母校。"},
    {"name": "天津大学", "province": "天津", "city": "天津", "ranking": 19, "website": "https://www.tju.edu.cn/", "description": "天津大学其前身为北洋大学，始建于1895年，是中国第一所现代大学。"},
    {"name": "华东师范大学", "province": "上海", "city": "上海", "ranking": 20, "website": "https://www.ecnu.edu.cn/", "description": "华东师范大学成立于1951年，是教育部直属、教育部与上海市共建的首批全国重点高校。"},
    {"name": "中南大学", "province": "湖南", "city": "长沙", "ranking": 21, "website": "https://www.csu.edu.cn/", "description": "中南大学是教育部直属全国重点大学，是国家211工程和985工程部省重点共建的高水平大学。"},
    {"name": "山东大学", "province": "山东", "city": "济南", "ranking": 22, "website": "https://www.sdu.edu.cn/", "description": "山东大学是一所历史悠久、学科齐全、学术实力雄厚的教育部直属重点综合性大学。"},
    {"name": "厦门大学", "province": "福建", "city": "厦门", "ranking": 23, "website": "https://www.xmu.edu.cn/", "description": "厦门大学由著名爱国华侨领袖陈嘉庚先生于1921年创办，是中国近代教育史上第一所华侨创办的大学。"},
    {"name": "湖南大学", "province": "湖南", "city": "长沙", "ranking": 24, "website": "https://www.hnu.edu.cn/", "description": "湖南大学坐落于中国历史文化名城长沙，校区坐落在湘江之滨、岳麓山下。"},
    {"name": "华南理工大学", "province": "广东", "city": "广州", "ranking": 25, "website": "https://www.scut.edu.cn/", "description": "华南理工大学是教育部直属的、以理工科见长的、研究型全国重点大学。"},
    {"name": "大连理工大学", "province": "辽宁", "city": "大连", "ranking": 26, "website": "https://www.dlut.edu.cn/", "description": "大连理工大学是中国共产党在新中国成立前夕创办的第一所新型正规大学。"},
    {"name": "西北工业大学", "province": "陕西", "city": "西安", "ranking": 27, "website": "https://www.nwpu.edu.cn/", "description": "西北工业大学坐落于陕西西安，是一所以发展航空、航天、航海等领域为特色的多科性、研究型大学。"},
    {"name": "重庆大学", "province": "重庆", "city": "重庆", "ranking": 28, "website": "https://www.cqu.edu.cn/", "description": "重庆大学是教育部直属的全国重点大学，是国家211工程和985工程重点建设的高水平研究型综合性大学。"},
    {"name": "电子科技大学", "province": "四川", "city": "成都", "ranking": 29, "website": "https://www.uestc.edu.cn/", "description": "电子科技大学坐落于四川省成都市，是新中国第一所无线电大学。"},
    {"name": "吉林大学", "province": "吉林", "city": "长春", "ranking": 30, "website": "https://www.jlu.edu.cn/", "description": "吉林大学是教育部直属的全国重点综合性大学，坐落在吉林省长春市，始建于1946年。"},
    {"name": "中国农业大学", "province": "北京", "city": "北京", "ranking": 31, "website": "https://www.cau.edu.cn/", "description": "中国农业大学作为教育部直属高校，是我国现代农业高等教育的起源地。"},
    {"name": "东北大学", "province": "辽宁", "city": "沈阳", "ranking": 32, "website": "https://www.neu.edu.cn/", "description": "东北大学始建于1923年，是一所具有爱国主义光荣传统的大学。"},
    {"name": "兰州大学", "province": "甘肃", "city": "兰州", "ranking": 33, "website": "https://www.lzu.edu.cn/", "description": "兰州大学是教育部直属的全国重点综合性大学，是国家985工程和211工程重点建设高校之一。"},
    {"name": "北京师范大学", "province": "北京", "city": "北京", "ranking": 34, "website": "https://www.bnu.edu.cn/", "description": "北京师范大学是教育部直属重点大学，是一所以教师教育、教育科学和文理基础学科为主要特色的著名学府。"},
    {"name": "中国海洋大学", "province": "山东", "city": "青岛", "ranking": 35, "website": "https://www.ouc.edu.cn/", "description": "中国海洋大学是一所海洋和水产学科特色显著的教育部直属重点综合性大学。"},
    {"name": "中央民族大学", "province": "北京", "city": "北京", "ranking": 36, "website": "https://www.muc.edu.cn/", "description": "中央民族大学坐落于北京学府林立的海淀区，校园环境典雅，人文氛围浓郁。"},
    {"name": "西北农林科技大学", "province": "陕西", "city": "杨凌", "ranking": 37, "website": "https://www.nwafu.edu.cn/", "description": "西北农林科技大学地处陕西杨凌，是教育部直属、国家985工程和211工程重点建设高校。"},
    {"name": "国防科技大学", "province": "湖南", "city": "长沙", "ranking": 38, "website": "https://www.nudt.edu.cn/", "description": "国防科技大学是中央军委直属的综合性研究型高等教育院校，是军队唯一进入国家985工程建设行列的院校。"},
    {"name": "中国人民大学", "province": "北京", "city": "北京", "ranking": 39, "website": "https://www.ruc.edu.cn/", "description": "中国人民大学是中国共产党创办的第一所新型正规大学，是一所以人文社会科学为主的综合性研究型全国重点大学。"},
]

def import_data():
    added = 0
    updated = 0
    
    for uni_data in UNIVERSITIES_985:
        uni, created = University.objects.update_or_create(
            name=uni_data["name"],
            defaults={
                "province": uni_data["province"],
                "city": uni_data["city"],
                "ranking": uni_data["ranking"],
                "university_type": "985",
                "level": "本科",
                "website": uni_data["website"],
                "description": uni_data["description"],
            }
        )
        if created:
            added += 1
        else:
            updated += 1
    
    print(f"导入完成! 新增 {added} 所, 更新 {updated} 所985大学")
    print(f"数据库中共有 {University.objects.count()} 所大学")

if __name__ == "__main__":
    import_data()
