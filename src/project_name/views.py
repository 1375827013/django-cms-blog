import subprocess
import os
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def deploy_webhook(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    deploy_token = os.getenv('DEPLOY_TOKEN', 'X7k9pQ2mR4vL8nJ3wT6yB5eA1cD9fG0h')
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.replace('Token ', '')
    if token != deploy_token:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    return JsonResponse({'status': 'test ok', 'message': 'deploy endpoint works'}, status=200)


@csrf_exempt
def deploy_full(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    deploy_token = os.getenv('DEPLOY_TOKEN', 'X7k9pQ2mR4vL8nJ3wT6yB5eA1cD9fG0h')
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.replace('Token ', '')
    if token != deploy_token:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    try:
        project_dir = '/home/8210232126/django-cms-blog'
        src_dir = os.path.join(project_dir, 'src')
        os.chdir(project_dir)

        result = subprocess.run(['git', 'fetch', 'origin'], capture_output=True, text=True)
        if result.returncode != 0:
            return JsonResponse({'error': f'git fetch failed: {result.stderr}'}, status=500)

        result = subprocess.run(['git', 'reset', '--hard', 'origin/main'], capture_output=True, text=True)
        if result.returncode != 0:
            return JsonResponse({'error': f'git reset failed: {result.stderr}'}, status=500)

        venv_python = os.path.join(project_dir, 'myenv', 'bin', 'python')
        req_file = os.path.join(src_dir, 'requirements.txt')
        result = subprocess.run([venv_python, '-m', 'pip', 'install', '-r', req_file], capture_output=True, text=True)
        if result.returncode != 0:
            return JsonResponse({'error': f'pip install failed: {result.stderr}'}, status=500)

        manage_py = os.path.join(src_dir, 'manage.py')
        result = subprocess.run([venv_python, manage_py, 'migrate'], capture_output=True, text=True, cwd=src_dir)
        if result.returncode != 0:
            return JsonResponse({'error': f'migrate failed: {result.stderr}'}, status=500)

        result = subprocess.run([venv_python, manage_py, 'collectstatic', '--noinput'], capture_output=True, text=True, cwd=src_dir)
        if result.returncode != 0:
            return JsonResponse({'error': f'collectstatic failed: {result.stderr}'}, status=500)

        create_admin_script = os.path.join(src_dir, 'scripts', 'create_admin.py')
        if os.path.exists(create_admin_script):
            subprocess.run([venv_python, create_admin_script], capture_output=True, text=True, cwd=src_dir)

        return JsonResponse({'status': 'deployment successful, please reload manually'}, status=200)

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