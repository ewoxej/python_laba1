"""msgchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main import views as main_views
    
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('/', main_views.userProfile),
    path('admin/', admin.site.urls),
    path('stat/', main_views.messagesStat),
    path('accounts/profile/', main_views.userProfile),
    path('send/', main_views.sendMessage),
    path('chat/', main_views.chat),
]
handler404 = 'main.views.handler404'
