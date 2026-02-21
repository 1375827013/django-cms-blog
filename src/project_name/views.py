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