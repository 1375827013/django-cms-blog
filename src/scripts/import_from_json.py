# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'

import django
django.setup()

from django.core.management import call_command

fixture_file = BASE_DIR / 'fixtures' / 'initial_data.json'

if not fixture_file.exists():
    print(f'错误: 找不到数据文件 {fixture_file}')
    sys.exit(1)

print(f'正在导入数据: {fixture_file}')
call_command('loaddata', str(fixture_file))
print('数据导入成功!')
