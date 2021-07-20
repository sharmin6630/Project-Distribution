from os import renames
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from myapp.forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import CustomUser, Student_data, Teachers_data, Teacher_edu, Paper
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
from django.contrib.auth import get_user
from django.conf import settings
from django.core.files.storage import FileSystemStorage

IMAGE_FILES_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.


def start(request):
    '''
        starting or index page
    '''
    return render(request, 'start.html')

def login(request):
    '''
        authentication check, if true takes to profile
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print("user", user, username, password)
        if user is not None:
            if user.is_active:
                print("ok2")
                auth_login(request, user)
                print("ok2")
                return HttpResponseRedirect('profile')
                
            else:
                #messages.info(request, 'invalid credentials')
                print("invalid")
                return render(request, 'home.html')
        else:
            print("ok4")
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def contact(request):
    # sub = forms.ContactusForm()
    # if request.method == 'POST':
    #     sub = forms.ContactusForm(request.POST)
    #     if sub.is_valid():
    #         email = sub.cleaned_data['Email']
    #         name=sub.cleaned_data['Name']
    #         message = sub.cleaned_data['Message']
    #         #send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
    #         return render(request, 'quiz/contactussuccess.html')
    # return render(request, 'contact.html', {'form':sub})
    return render(request, 'contact.html')

# def contact(request):
#     if request.user.is_authenticated:
#         user_info = request.user
#         teacher_info = CustomUser.objects.filter(user_type="teacher")
#         student_info = CustomUser.objects.filter(user_type="student")
#         user_sd = Student_data.objects.get(user_id_id=request.user.id)
#         s_data_all = Student_data.objects.all()
#         return render(request, 'thesisform.html', {'user_in': user_info, 'user_sd': user_sd, 
#         'all_student': student_info, 'all_teacher': teacher_info, 's_data_all': s_data_all})
#     return render(request, 'home.html')

def form_save(request):
    '''
        save thesis form data then returns to user profile
    '''
    if request.user.is_authenticated and request.user.user_type=="student":
        if request.method == 'POST':
            student_1_id = request.user.id
            student_1_sd = Student_data.objects.get(user_id_id=student_1_id)
            student_2_id = request.POST.get('student_2_id')
            student_2_sd = Student_data.objects.get(user_id_id=student_2_id)
            student_2 = CustomUser.objects.get(id=student_2_id)
            Course = request.POST.get('Course')
            topic = request.POST.get('topic')
            description = request.POST.get('description')
            supervisor_1 = request.POST.get('supervisor_1')
            supervisor_2 = request.POST.get('supervisor_2')
            supervisor_3 = request.POST.get('supervisor_3')
            supervisor_4 = request.POST.get('supervisor_4')
            supervisor_5 = request.POST.get('supervisor_5')
            sup_1 = CustomUser.objects.get(id=supervisor_1)
            sup_2 = CustomUser.objects.get(id=supervisor_2)
            sup_3 = CustomUser.objects.get(id=supervisor_3)
            sup_4 = CustomUser.objects.get(id=supervisor_4)
            sup_5 = CustomUser.objects.get(id=supervisor_5)
            external = request.POST.get('external')
            student_1_name = request.user.first_name + " " + request.user.last_name
            student_1_username = request.user.username
            student_2_name = student_2.first_name + " " + student_2.last_name
            student_2_username = student_2.username
            # supervisor_1_name = sup_1.first_name + " " + sup_1.last_name
            supervisor_1_name = sup_1.username
            supervisor_2_name = sup_2.first_name + " " + sup_2.last_name
            supervisor_2_name = sup_2.username
            supervisor_3_name = sup_3.first_name + " " + sup_3.last_name
            supervisor_3_name = sup_3.username
            supervisor_4_name = sup_4.first_name + " " + sup_4.last_name
            supervisor_4_name = sup_4.username
            supervisor_5_name = sup_5.first_name + " " + sup_5.last_name
            supervisor_5_name = sup_5.username
            x = compact_Form.objects.filter(student_1_id_id=student_1_id).count()
            y = compact_Form.objects.filter(student_1_id_id=student_2_id).count()
            if x != 0 or y!=0:
                exist_check = None
                if x != 0:
                    exist_check = compact_Form.objects.get(student_1_id_id=student_1_id)
                    print("Duplicate")
                    exist_check.student_1_id_id=student_1_id
                    exist_check.student_1_name=student_1_name
                    exist_check.student_1_username=student_1_username
                    exist_check.student_2_id=student_2_id
                    exist_check.student_2_name=student_2_name
                    exist_check.student_1_majorcg=student_1_sd.major_cgpa
                    exist_check.student_1_totalcg=student_1_sd.total_cgpa
                    exist_check.student_2_majorcg=student_2_sd.major_cgpa
                    exist_check.student_2_totalcg=student_2_sd.total_cgpa
                    exist_check.student_2_username=student_2_username
                else:
                    exist_check = compact_Form.objects.get(student_1_id_id=student_2_id)
                    exist_check.student_1_id_id=student_2_id
                    exist_check.student_1_name=student_2_name
                    exist_check.student_1_username=student_2_username
                    exist_check.student_2_name=student_1_name
                    exist_check.student_2_id=student_1_id
                    exist_check.student_1_majorcg=student_2_sd.major_cgpa
                    exist_check.student_1_totalcg=student_2_sd.total_cgpa
                    exist_check.student_2_majorcg=student_1_sd.major_cgpa
                    exist_check.student_2_totalcg=student_1_sd.total_cgpa
                    exist_check.student_2_username=student_1_username
                exist_check.Course=Course
                exist_check.topic=topic
                exist_check.description=description
                exist_check.supervisor_1=supervisor_1 
                exist_check.supervisor_2=supervisor_2
                exist_check.supervisor_3=supervisor_3
                exist_check.supervisor_4=supervisor_4
                exist_check.supervisor_5=supervisor_5
                exist_check.supervisor_1_name=supervisor_1_name 
                exist_check.supervisor_2_name=supervisor_2_name
                exist_check.supervisor_3_name=supervisor_3_name
                exist_check.supervisor_4_name=supervisor_4_name
                exist_check.supervisor_5_name=supervisor_5_name
                exist_check.external=external
                exist_check.save()
            else:
                form_up = compact_Form(student_1_id_id=student_1_id, student_2_id=student_2_id,
                student_1_username=student_1_username, student_2_username= student_2_username,  
                student_1_majorcg=student_1_sd.major_cgpa, 
                student_1_totalcg=student_1_sd.total_cgpa,
                student_2_majorcg=student_2_sd.major_cgpa,
                student_2_totalcg=student_2_sd.total_cgpa,
                student_1_name=student_1_name,student_2_name=student_2_name,
                Course=Course, topic=topic, description=description, 
                supervisor_1=supervisor_1, supervisor_2=supervisor_2, 
                supervisor_3=supervisor_3, supervisor_4=supervisor_4, 
                supervisor_5=supervisor_5, external=external,
                supervisor_1_name=supervisor_1_name, supervisor_2_name=supervisor_2_name,
                supervisor_3_name=supervisor_3_name, supervisor_4_name=supervisor_4_name,
                supervisor_5_name=supervisor_5_name)
                form_up.save()
        return HttpResponseRedirect('profile')
    else:
        return render(request, 'home.html')


def about(request):
    '''
        takes to about page
    '''
    return render(request,'about.html')

def adminclick(request):
    if request.user.is_authenticated:
        all_form = compact_Form.objects.all()
        all_teacher = CustomUser.objects.filter(user_type="teacher")
        return render(request,'form_table_admin compact.html', {'all_form': all_form, 'all_teacher': all_teacher})
    else:
        return render(request,'home.html')

def filter_form(request):
    if request.user.is_authenticated:
        query = float(request.GET.get("q"))
        print(float(query))
        if query:
            form_x = compact_Form.objects.all()
            all_form = []
            for x in form_x:
                if x.student_1_majorcg >= query and x.student_2_majorcg >= query:
                    all_form.append(x)
            all_teacher = CustomUser.objects.filter(user_type="teacher")
            return render(request,'form_table_admin compact.html', {'all_form': all_form, 'all_teacher': all_teacher})
    else:
        return render(request,'home.html')


def tasks(request):
    if request.user.is_authenticated:
        user_info = request.user
        teacher_info = CustomUser.objects.filter(user_type="teacher")
        pre_student_info = CustomUser.objects.filter(user_type="student")
        student_info = []
        for x in pre_student_info:
            if x.id != request.user.id:
                student_info.append(x)

        #student_info = student_info.filter(id != request.user.id)
        user_sd = Student_data.objects.get(user_id_id=request.user.id)
        #s_data_all = Student_data.objects.all()
        return render(request, 'thesisform.html', {'user_in': user_info, 
        'user_sd': user_sd, 'all_student': student_info, 'all_teacher': teacher_info})
    return render(request, 'home.html')

def teacherclick(request):
    return render(request,'teacherclick.html')

def studentclick(request):
    return render(request,'studentclick.html')

def register(request):
    '''
        user registration is done and login page is loaded
    '''
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = CustomUser(username=username, user_type=user_type, first_name=first_name, last_name=last_name, email=email, password=password)
        print("user created")
        user.set_password(password)
        user.is_active = True
        user.save()
        return HttpResponseRedirect('login')
    else:
        return render(request,'register.html')

def profile(request):
    '''
        loads profile based on user type, 
        if not false to login page
    '''
    if request.user.is_authenticated:
        user_info = request.user
        if (user_info.user_type == "student"):
            x = Student_data.objects.filter(user_id_id=request.user.id).count()
            if x != 0:
                s_id = Student_data.objects.get(user_id_id=request.user.id)
                return render(request, 'profile_student.html', {'user_in': user_info, 'user_sd': s_id})
            else:
                return render(request, 'profile_student.html', {'user_in': user_info, 'user_sd': user_info})

        elif (user_info.user_type == "teacher"):
            x = Teachers_data.objects.filter(user_id_id=request.user.id).count()
            if x != 0:
                s_id = Teachers_data.objects.get(user_id_id=request.user.id)
                return render(request, 'profile_teacher.html', {'user_in': user_info, 'user_sd': s_id})
            else:
                return render(request, 'profile_teacher.html', {'user_in': user_info, 'user_sd': user_info})

        elif (user_info.user_type == "admin"):
            return render(request, 'profile_admin_test.html', {'user_in': user_info})
    else:
        #messages.info(request, 'invalid credentials')
        print("invalid")
        return render(request, 'home.html')

def search(request):
    if request.user.is_authenticated:
        user_info = request.user
        all_teacher = CustomUser.objects.filter(user_type="teacher")
        td = []
        for x in all_teacher:
            y = None
            see = Teachers_data.objects.filter(user_id_id=x.id).count()
            if see != 0:
                y = Teachers_data.objects.get(user_id_id=x.id)
            td.append(y)
        return render(request, 'search.html', {'user_in': user_info, 'all_teacher': zip(all_teacher,td)})
    else:
        return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('login')

def student_update(request):
    user_info = request.user
    x = Student_data.objects.filter(user_id_id=request.user.id).count()
    if x != 0:
        s_id = Student_data.objects.get(user_id_id=request.user.id)
        return render(request, 'student_update.html', {'user_in': user_info, 'user_sd': s_id})
    else:
        return render(request, 'student_update.html', {'user_in': user_info, 'user_sd': user_info})

def student_save(request):
    user_info = request.user
    print(request.method, "hihi")
    if request.method == 'POST':
        print(request.FILES["photos"])
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        mobile_no = request.POST.get('mobile_no')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        total_cgpa = request.POST.get('total_cgpa')
        major_cgpa = request.POST.get('major_cgpa')
        github = request.POST.get('github')
        linkedin = request.POST.get('linkedin')
        photos = request.FILES["photos"]
        user = authenticate(request, username=request.user.username, password=password)
        if user is None:
            print("not authenticated, no update")
            return HttpResponseRedirect('profile')
        x = Student_data.objects.filter(user_id_id=request.user.id).count()
        if x != 0:
            exist_check = Student_data.objects.get(user_id_id=request.user.id)
            exist_check.mobile_no=mobile_no
            exist_check.user_id_id=user_info.id
            exist_check.address=address
            exist_check.blood_group=blood_group
            exist_check.total_cgpa=total_cgpa 
            exist_check.major_cgpa=major_cgpa 
            exist_check.github=github
            exist_check.linkedin=linkedin
            exist_check.photos=request.FILES["photos"]
            exist_check.save()
        else:        
            st_up = Student_data(mobile_no=mobile_no, user_id_id=user_info.id,
            address=address, blood_group=blood_group, total_cgpa=total_cgpa, 
            major_cgpa=major_cgpa, github=github, linkedin=linkedin, photos=request.FILES["photos"])
            st_up.save()
        user_info = CustomUser.objects.get(id=request.user.id)
        user_info.first_name=first_name
        user_info.last_name=last_name
        user_info.email=email
        if len(new_password) != 0:
            print("user password updated")
            user_info.set_password(new_password)
        user_info.is_active = True
        user_info.save()
        x = Student_data.objects.filter(user_id_id=request.user.id).count()
        return HttpResponseRedirect('profile')
    else:
        return render(request,'home.html')

def teacher_update(request):
    user_info = request.user
    x = Teachers_data.objects.filter(user_id_id=request.user.id).count()
    if x != 0:
        s_id = Teachers_data.objects.get(user_id_id=request.user.id)
        return render(request, 'teacher_update.html', {'user_in': user_info, 'user_sd': s_id})
    else:
        return render(request, 'teacher_update.html', {'user_in': user_info, 'user_sd': user_info})

def teacher_save(request):
    user_info = request.user
    print(request.method, "teacher up")
    if request.method == 'POST':
        print(request.FILES["photos"])
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        mobile_no = request.POST.get('mobile_no')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        sust_id = request.POST.get('sust_id')
        scholar = request.POST.get('scholar')
        photos = request.FILES["photos"]
        designation = request.POST.get('designation')
        user = authenticate(request, username=request.user.username, password=password)
        if user is None:
            print("not authenticated, no update")
            return HttpResponseRedirect('profile')
        x = Teachers_data.objects.filter(user_id_id=request.user.id).count()
        if x != 0:
            exist_check = Teachers_data.objects.get(user_id_id=request.user.id)
            exist_check.mobile_no=mobile_no
            exist_check.user_id_id=user_info.id
            exist_check.address=address
            exist_check.blood_group=blood_group
            exist_check.sust_id=sust_id
            exist_check.scholar=scholar
            exist_check.designation=designation
            exist_check.photos=request.FILES["photos"]
            exist_check.save()
        else:        
            tc_up = Teachers_data(mobile_no=mobile_no, user_id_id=user_info.id,
            address=address, blood_group=blood_group,  sust_id=sust_id, 
            scholar=scholar, designation=designation, photos=request.FILES["photos"])
            tc_up.save()
        user_info = CustomUser.objects.get(id=request.user.id)
        user_info.first_name=first_name
        user_info.last_name=last_name
        user_info.email=email
        if len(new_password) != 0:
            print("user password updated")
            user_info.set_password(new_password)
        user_info.is_active = True
        user_info.save()
        return HttpResponseRedirect('profile')
    else:
        return render(request,'home.html')


def see_teacher(request, id):
    '''
        students can see the requested teacher profile
    '''
    if request.user.is_authenticated:
        user_info = request.user
        teacher = CustomUser.objects.get(id=id)
        td = None
        x = Teachers_data.objects.filter(user_id_id=teacher.id).count()
        if x != 0:
            td = Teachers_data.objects.get(user_id_id=teacher.id)
        return render(request, 'see_teacher.html', {'user_in': teacher, 'user_sd': td})
    else:
        return render(request, 'home.html')

def form_approve(request, id):
    '''
        students are assigned to supervisor
    '''
    if request.user.is_authenticated and request.user.user_type=="admin":
        if request.method == 'POST':
            form_record = compact_Form.objects.get(id=id)
            assigned_supervisor_id = request.POST.get('assigned_supervisor_id')
            assigned_course = request.POST.get('assigned_course')
            assigned_external = request.POST.get('assigned_external')
            print(assigned_external)
            print(assigned_supervisor_id)
            sup = CustomUser.objects.filter(id=assigned_supervisor_id).count()
            if sup == 0:
                return render(request, 'home.html')
            sup = CustomUser.objects.get(id=assigned_supervisor_id)
            assigned_supervisor = sup.username
            form_record.assigned_supervisor_id = assigned_supervisor_id
            form_record.assigned_course = assigned_course
            form_record.assigned_external = assigned_external
            form_record.assigned_supervisor = assigned_supervisor
            form_record.action = "Assigned"
            form_record.save()
            return redirect('adminclick')
    else:
        return render(request, 'home.html')

# def plot_show(request):
#     all_form = Form.objects.all()
#     all_teacher = CustomUser.objects.filter(user_type="teacher")
#     user_info = request.user
#     return render(request, 'plot_show.html', {'user_in': user_info, 'all_form': all_form, 'all_teacher': all_teacher})


def pie_chart(request):
    print("pie_chart")
    data=[]
    labels=["Thesis", "project"]
    queryset = Student_data.objects.all()
    count_ma=0
    count_mi=0
    count=0
    total=0
    
    for c in queryset:
        total=total+1
        if c.major_cgpa>=3.5:
            count_ma=count_ma+1
            
        if c.total_cgpa>=3.5:
            count_mi=count_mi+1

        if c.major_cgpa>=3.5 and c.total_cgpa>=3.5:
            count=count+1

    thesis= count
    project= total-count
        
    data.append(thesis)
    data.append(project)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })



def line_chart(request):
    data=[]
    labels=["Major", "Total","Major and Total", "CGPA less than 2"]
    queryset = Student_data.objects.all()
    count_ma=0
    count_mi=0
    count=0
    cnt_2 = 0
    for c in queryset:
        if c.major_cgpa>=3.5:
            count_ma=count_ma+1
            
        if c.total_cgpa>=3.5:
            count_mi=count_mi+1
        
        if c.major_cgpa>=3.5 and c.total_cgpa>=3.5:
            count=count+1
        if c.major_cgpa < 2 and c.total_cgpa < 2:
            cnt_2 += 1
    data.append(count_ma)
    data.append(count_mi)
    data.append(count)
    data.append(cnt_2)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def home1(request):
    return render(request, 'home1.html')