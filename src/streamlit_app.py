import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://xgwgtlealmcynvizozfd.supabase.co')
SUPABASE_KEY = os.getenv('SUPABASE_ANON_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhnd2d0bGVhbG1jeW52aXpvemZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI0NTY5MjAsImV4cCI6MjA4ODAzMjkyMH0.r1joKATw33DycNJzSzY0sEOR0TPop3xN0GnGmhYlRxc')

st.set_page_config(page_title="考研数据查询", page_icon="📚", layout="wide")

PROVINCE_REGION_MAP = {
    "华北": ["北京", "天津", "河北", "山西", "内蒙古"],
    "东北": ["辽宁", "吉林", "黑龙江"],
    "华东": ["上海", "江苏", "浙江", "安徽", "福建", "江西", "山东"],
    "华中": ["河南", "湖北", "湖南"],
    "华南": ["广东", "广西", "海南"],
    "西南": ["重庆", "四川", "贵州", "云南", "西藏"],
    "西北": ["陕西", "甘肃", "青海", "宁夏", "新疆"],
    "港澳台": ["香港", "澳门", "台湾"]
}

if 'all_expanded' not in st.session_state:
    st.session_state.all_expanded = False

@st.cache_resource
def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_schools(client):
    return client.table('schools').select('*').execute().data

def get_provinces(client):
    return client.table('provinces').select('*').execute().data

def get_categories(client):
    return client.table('categories').select('*').execute().data

def group_schools_by_province(schools, provinces):
    province_map = {p['code']: p['name'] for p in provinces}
    
    province_schools = {}
    
    for school in schools:
        province_code = school.get('province_code')
        province_name = province_map.get(province_code, "未知")
        
        if province_name not in province_schools:
            province_schools[province_name] = []
        
        province_schools[province_name].append({
            **school,
            'province_name': province_name
        })
    
    sorted_provinces = sorted(province_schools.items(), key=lambda x: len(x[1]), reverse=True)
    
    return sorted_provinces

st.title("📚 考研数据查询系统")

menu = st.sidebar.selectbox("功能选择", ["按省份查院校", "搜索院校", "专业类别"])

if menu == "按省份查院校":
    client = get_supabase_client()
    provinces = get_provinces(client)
    schools = get_all_schools(client)
    province_schools = group_schools_by_province(schools, provinces)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.subheader(f"共 {len(schools)} 所院校")
    with col2:
        if st.button("📂 全部展开", use_container_width=True):
            st.session_state.all_expanded = True
            st.rerun()
    with col3:
        if st.button("📁 全部收纳", use_container_width=True):
            st.session_state.all_expanded = False
            st.rerun()
    
    for province_name, school_list in province_schools:
        if school_list:
            with st.expander(f"📍 {province_name} ({len(school_list)} 所)", expanded=st.session_state.all_expanded):
                for school in school_list:
                    st.write(f"**{school['mc']}** ({school['dm']})")

elif menu == "搜索院校":
    client = get_supabase_client()
    provinces = get_provinces(client)
    
    search = st.text_input("搜索院校名称或代码", "")
    
    if search:
        schools = client.table('schools').select('*').or_(f'mc.ilike.%{search}%,dm.ilike.%{search}%').execute().data
        st.subheader(f"找到 {len(schools)} 所院校")
        
        for school in schools:
            province_name = "未知"
            for p in provinces:
                if p['code'] == school.get('province_code'):
                    province_name = p['name']
                    break
            
            with st.expander(f"📖 {school['mc']}"):
                st.write(f"**院校代码:** {school['dm']}")
                st.write(f"**所在省份:** {province_name}")
                if school.get('href'):
                    st.write(f"**相关链接:** {school['href']}")
    else:
        st.info("请输入院校名称或代码进行搜索")

elif menu == "专业类别":
    client = get_supabase_client()
    categories = get_categories(client)
    
    st.subheader(f"共 {len(categories)} 个专业类别")
    
    cols = st.columns(3)
    for i, cat in enumerate(categories):
        with cols[i % 3]:
            st.info(f"**{cat['mc']}**\n\n代码: {cat['dm']}")

st.sidebar.markdown("---")
st.sidebar.info("数据来源: Supabase")
