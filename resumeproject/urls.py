"""resumeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="homePage"),
    path('',include('services.urls')),
    path('',include('edu.urls')),
    path('contact/',views.contact, name="contactPage"),
]


# ! FOR HOSTING 
# pip freeze / to list our pkgs library project is using
# pip freeze > requirements.txt
# STATIC_ROOT = BASE_DIR / 'static/' (settings.py) / to get all static files from apps
# COMPRESS FOLDER TO ZIP
# pythonanywhere.com / create account
# UPLOAD FILE /files
# Consoles > bash
# ? COMMANDS  ! (YOUR PYTHON VERSION WHICH U HAVE USED TO CREATE THIS PROJECT)
# mkvirtualenv nameEnv --python=/usr/bin/python3.8 >enter
# (nameEnv) 1:2 // ACTIVE ENV
# if not active type > workon nameEnv 
# unzip resumeproject > enter
# Web tab > add new app > manual config > py 3.8 >
# find Virtualenv  > Enter path > nameEnv
# cd resumeproject/
# pip install -r requirements.txt
# > goto web > Code: open wsgi file
# edit wsgi file keep Django code 
# check video 
# To collect static files
# python manage.py collectstatic > enter 