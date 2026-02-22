import os
import sys
from pathlib import Path

BASE_DIR = Path(r'e:\Documents\Trae_Project\project_name\src')
sys.path.insert(0, str(BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'

import django
django.setup()

from django.core.management import call_command

output_file = BASE_DIR / 'data_dump.json'
print(f'准备写入文件: {output_file}')
print(f'目录存在: {BASE_DIR.exists()}')

try:
    with open(output_file, 'w', encoding='utf-8') as f:
        call_command('dumpdata', 'app_name', stdout=f, indent=2)
    
    file_size = output_file.stat().st_size
    print(f'数据导出成功！')
    print(f'文件大小: {file_size} 字节')
except Exception as e:
    print(f'错误: {e}')
    import traceback
    traceback.print_exc()
