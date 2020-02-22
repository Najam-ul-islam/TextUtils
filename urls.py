"""mySite URL Configuration

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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # Here name=index is a function which is defined in views.py
    path('', views.index, name="index"),
    path('analyze', views.analyze, name="analyze"),

    # path('about', views.about, name="about"),
    # path('file_content', views.file_content, name="file_content"),
    # path('personal_navigator', views.personal_navigator, name="personal_navigator"),
    # path('removepunc', views.removepunc, name="remove punc"),
    # path('capatilizefirst', views.capatilizefirst, name="capatilize first"),
    # path('newlineremove', views.newlineremove, name="new line remove"),
    # path('spaceremove', views.spaceremove, name="space remove"),
    # path('charcount', views.charcount, name="char count"),

]
