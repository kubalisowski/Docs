"""DjangoURL URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from basicapp import views

urlpatterns = [
    ### Directly calling the function from views.py (from app folder)
    url(r'^$', views.index, name='index'),
    ### Go to app/urls.py to get the next piece of url and actions (https//something.com/basicapp/[+mapping from app/ulrs.py]
    url(r'^basicapp/', include('basicapp.urls')),
    ### Admin panel
    url('admin/', admin.site.urls),
]
