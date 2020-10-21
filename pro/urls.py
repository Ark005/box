"""pro URL Configuration

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
from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static 
from posts.views import blog_view
from django.http import HttpResponse
from posts import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')), 
    path('home.html', include('posts.urls')), 
    path('contacts.html', include('posts.urls')), 
    path('about.html', include('posts.urls')),
    path('box.html', include('posts.urls')), 
    path('box1.html', include('posts.urls')), 
    path('box2.html', include('posts.urls')), 
    path('box3.html', include('posts.urls')), 
    path('box4.html', include('posts.urls')), 
    path('box5.html', include('posts.urls')), 
    path('production.html', include('posts.urls')), 
    path('blog.html', views.blog_view, name='blog'),
    path('product.detail.html', views.blog1_view, name='blog'),  
    path('<int:id>/', views.detail_view, name='detail'),
    # path('about', views.about), 
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

