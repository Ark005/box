from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
  
    boxView,
    postBox,
    checkNickName,
    BoxView,
    boxView1,
    boxView2,
    boxView3,
    boxView4,
    boxView5,
    home_view,
    blog_view,
    production_view,
    about_view,
    contacts_view
    
)

urlpatterns = [
    path('',  home_view),
    path('production.html',  production_view),
    path('about.html', about_view),
    path('contacts.html',  contacts_view),
    path('about.html', about_view),
    path('blog.html', blog_view),
    path('box.html', boxView),
    path('box1.html', boxView1),
    path('box2.html', boxView2),
    path('box3.html', boxView3),
    path('box4.html', boxView4),
    path('box5.html', boxView5),
    path('post/ajax/box', postBox, name = "post_box"),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),

]