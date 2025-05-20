"""
URL configuration for job_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   
from django.http import JsonResponse

from django.conf import settings
from django.conf.urls.static import static


# 使用者登入、登出、註冊
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,  # 如果你要實作 logout
)
from apps.users.views import RegisterView


def home(request):
    return JsonResponse({'message': 'Welcome to the API homepage!'})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # 先註解掉，等有新增urls時再開啟
    path('api/companies/', include('apps.companies.urls')),
    path('api/jobs/', include('apps.jobs.urls')),
    path('api/users/', include('apps.users.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
