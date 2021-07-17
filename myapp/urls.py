from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.start, name='start'),
    path('login', views.login, name='login'), ##login
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('studentclick', views.studentclick, name='studentclick'),
    path('teacherclick', views.teacherclick, name='teacherclick'),
    path('adminclick', views.adminclick, name='adminclick'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('student_update', views.student_update, name='student_update'),
    path('teacher_update', views.teacher_update, name='teacher_update'),
    path('teacher_save', views.teacher_save, name='teacher_save'),
    path('student_save', views.student_save, name='student_save'),
    path('form_save', views.form_save, name='form_save'),
    path('<int:id>/form_approve', views.form_approve, name='form_approve'),
    path('tasks', views.tasks, name='tasks'),
    path('<int:id>/see_teacher/', views.see_teacher, name='see_teacher'),
    # path('plot_show', views.plot_show, name='plot_show'),
    path('filter_form',views.filter_form,name='filter_form'),
    path('plot_show', views.home1, name='home1'),
    path('pie-chart', views.pie_chart, name='pie-chart'),
    path('population-chart', views.line_chart, name='population-chart'),
    
    # path('<int:id>/phd/',views.phd,name='phd'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)