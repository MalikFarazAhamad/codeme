from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("python", views.python , name='python'),
    path("ruby",views.ruby,name='ruby'),
    path("css", views.css, name='css'),
    path("boost",views.boost,name='boost'),
    path("web",views.web,name='web'),
    path("java",views.java,name='java'),
    path("c",views.c,name='c'),
    path("cpp",views.cpp, name='cpp'),
    path("contact", views.contact, name='contact'), 
]