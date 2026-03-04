import subprocess
import os
import requests
from django.http import JsonResponse
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

        venv_python = '/usr/bin/python3'
        if os.path.exists(os.path.join(project_dir, 'myenv', 'bin', 'python')):
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

        import_script = os.path.join(src_dir, 'scripts', 'import_from_json.py')
        if os.path.exists(import_script):
            result = subprocess.run([venv_python, import_script], capture_output=True, text=True, cwd=src_dir)
            if result.returncode != 0:
                return JsonResponse({'warning': f'data import had issues: {result.stderr}', 'status': 'deployment successful'}, status=200)

        api_token = os.getenv('PYTHONANYWHERE_API_TOKEN')
        username = '8210232126'
        domain = '8210232126.pythonanywhere.com'
        
        if api_token:
            reload_url = f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'
            headers = {'Authorization': f'Token {api_token}'}
            reload_response = requests.post(reload_url, headers=headers)
            if reload_response.status_code == 200:
                return JsonResponse({'status': 'deployment successful, auto-reloaded'}, status=200)
        
        return JsonResponse({'status': 'deployment successful, please reload manually'}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500})


@csrf_exempt
def create_admin_view(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
