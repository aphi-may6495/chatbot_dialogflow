"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blogs import views
from chatbot import views as cbv
from chatbot.views import webhook_facebook  
from chatbot.views import webhook_dialogflow_es

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('test/', cbv.test),
    # path('webhook_facebook', cbv.webhook_facebook, name = 'webhook_facebook'),
    path('webhook_facebook', webhook_facebook.as_view() , name='webhook_facebook'),
    path('webhook_dialogflow_es', webhook_dialogflow_es.as_view() , name='webhook_dialogflow_es'),
]
