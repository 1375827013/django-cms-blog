from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='app_name/', permanent=False)),
    path('rocket/', TemplateView.as_view(template_name='default_index.html'), name='rocket'),
    path('admin/', admin.site.urls),
    path('app_name/', include('app_name.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('deploy/', views.deploy_webhook, name='deploy'),
    path('deploy-full/', views.deploy_full, name='deploy_full'),
    path('create-admin/', views.create_admin_view, name='create_admin'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)