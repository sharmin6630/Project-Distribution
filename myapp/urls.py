from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('studentclick', views.studentclick, name='studentclick'),
    path('teacherclick', views.teacherclick, name='teacherclick'),
    path('adminclick', views.adminclick, name='adminclick'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]