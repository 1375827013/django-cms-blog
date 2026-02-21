from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = '创建或重置管理员账号'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = 'admin'
        password = 'admin123456'
        email = 'admin@example.com'
        
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'✅ 管理员密码已重置'))
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'✅ 管理员账号已创建'))
        
        self.stdout.write(f'用户名: {username}')
        self.stdout.write(f'密码: {password}')