"""portfolio URL Configuration


"""
from django.contrib import admin
from django.urls import path,include
from webapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('pro/',include('projects.urls')),
    path('skill/',include('skills.urls')),
]
