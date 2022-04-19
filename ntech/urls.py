"""ntech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ntech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about_us/', views.about_us),
    path('industry/', views.industry),
    path('other/', views.other),
    path('contact_us/', views.contact_us),
    path('coverage/', views.coverage),
    path('join_our_panel/', views.join_our_panel),
    path('qualitative/', views.qualitative),
    path('quantitative/', views.quantitative),
    
]
