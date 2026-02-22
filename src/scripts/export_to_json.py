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

output_file = BASE_DIR / 'fixtures' / 'initial_data.json'
output_file.parent.mkdir(exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    call_command('dumpdata', 
        'app_name.University',
        'app_name.Major', 
        'app_name.AdmissionScore',
        'app_name.StudentProfile',
        'app_name.CollegePreference',
        stdout=f, 
        indent=2,
        use_natural_foreign_keys=True
    )

print(f'数据导出成功: {output_file}')
print(f'文件大小: {output_file.stat().st_size} 字节')
