import subprocess
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

DEPLOY_TOKEN = os.getenv('DEPLOY_TOKEN', '')

@csrf_exempt
def deploy_webhook(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    auth_header = request.headers.get('Authorization', '')
    token = auth_header.replace('Token ', '')
    if token != DEPLOY_TOKEN:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    try:
        project_dir = '/home/8210232126/django-cms-blog'
        os.chdir(project_dir)

        subprocess.run(['git', 'fetch', 'origin'], check=True, capture_output=True, text=True)
        subprocess.run(['git', 'reset', '--hard', 'origin/main'], check=True, capture_output=True, text=True)

        venv_python = os.path.join(project_dir, 'myenv', 'bin', 'python')
        subprocess.run([venv_python, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)

        subprocess.run([venv_python, 'manage.py', 'migrate'], check=True)

        subprocess.run([venv_python, 'manage.py', 'collectstatic', '--noinput'], check=True)

        subprocess.run([venv_python, 'create_admin.py'], capture_output=True, text=True)

        import requests
        api_url = "https://www.pythonanywhere.com/api/v0/user/8210232126/webapps/8210232126.pythonanywhere.com/reload/"
        headers = {"Authorization": f"Token {settings.PYTHONANYWHERE_API_TOKEN}"}
        r = requests.post(api_url, headers=headers)
        if r.status_code != 200:
            return JsonResponse({'warning': '部署完成但重载 API 调用失败，请手动重载'}, status=500)

        return JsonResponse({'status': 'deployment successful'}, status=200)

    except subprocess.CalledProcessError as e:
        return JsonResponse({'error': e.stderr}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def create_admin_view(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    username = 'admin'
    password = 'admin123456'
    email = 'admin@example.com'
    
    try:
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return JsonResponse({
                'status': 'password reset',
                'username': username,
                'password': password
            })
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            return JsonResponse({
                'status': 'created',
                'username': username,
                'password': password
            })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)