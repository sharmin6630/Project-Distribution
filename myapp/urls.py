from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.start, name='start'), #start
    path('login', views.login, name='login'), #login
    path('about', views.about, name='about'), #about
    path('contact', views.contact, name='contact'), #contact
    path('form_output', views.form_output, name='form_output'), #form_outputs
    path('register', views.register, name='register'), #register
    path('search', views.search, name='search'), #search_teachers
    path('profile', views.profile, name='profile'), #profile
    path('logout', views.logout, name='logout'), #logout
    path('student_update', views.student_update, name='student_update'), #student data update
    path('teacher_update', views.teacher_update, name='teacher_update'), #teacher data update
    path('teacher_save', views.teacher_save, name='teacher_save'), #teacher data save
    path('student_save', views.student_save, name='student_save'), #student data save
    path('form_save', views.form_save, name='form_save'), #form save
    path('<int:id>/form_approve', views.form_approve, name='form_approve'), #form data approve
    path('tasks', views.tasks, name='tasks'), #student form fill
    path('<int:id>/see_teacher/', views.see_teacher, name='see_teacher'), #teacher profile visit
    path('not_allowed', views.not_allowed, name='not_allowed'), #forbidden message
    # path('plot_show', views.plot_show, name='plot_show'),
    path('filter_form',views.filter_form,name='filter_form'), #filter student based on cgpa
    path('plot_show', views.home1, name='home1'),
    path('pie-chart', views.pie_chart, name='pie-chart'),
    path('population-chart', views.line_chart, name='population-chart'),
    path('search_user', views.search_user, name='search_user'), #search_users
    path('<int:id>/see_student/', views.see_student, name='see_student'), #student profile visit
    path('filter_user_type', views.filter_user_type, name='filter_user_type'),
    # path('<int:id>/phd/',views.phd,name='phd'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)