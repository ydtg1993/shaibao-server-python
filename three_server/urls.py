"""three_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from three_server.api.server_auth import login, logout
from three_server.api.client_auth import client_login, client_registered, client_reset_password, send_code
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('chat/', include('notice.urls')),
    path('admin/', admin.site.urls),
    # 后台认证接口
    path('auth/login', login, name='login'),
    path('auth/logout', logout, name='logout'),
    # 客户端认证接口
    path('auth/client/login', client_login, name='login'),
    path('auth/client/registered', client_registered, name='registered'),
    path('auth/client/reset_password', client_reset_password, name='reset_password'),
    path('auth/client/send_code', send_code, name='send_code'),
    # 客户业务接口
    re_path('^three/hall/', include('hall.client_router')),
    re_path('^three/player/', include('player.client_router')),
    re_path('^three/mail/', include('mail.client_router')),
    re_path('^three/announcement/', include('announcement.client_router')),
    re_path('^three/sign/', include('sign.client_router')),
    re_path('^three/finance/', include('finance.client_router')),
    # 后台业务接口
    re_path('^api/system/', include('system.router')),
    re_path('^api/player/', include('player.server_router')),
    re_path('^api/hall/', include('hall.server_router')),
    re_path('^api/mail/', include('mail.server_router')),
    re_path('^api/announcement/', include('announcement.server_router')),
    re_path('^api/sign/', include('sign.server_router')),
    re_path('^api/finance/', include('finance.server_router')),
    re_path('^api/setting/', include('game_setting.server_router')),
]
