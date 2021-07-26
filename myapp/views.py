from os import renames
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from myapp.forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import CustomUser, Student_data, Teachers_data, Teacher_edu, Paper, compact_Form, Notice
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

IMAGE_FILES_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.


def start(request):
    '''
        starting or index page
    '''
    return render(request, 'start.html')

def about(request):
    '''
        takes to about page
    '''
    return render(request,'about.html')

def register(request):
    '''
        user registration is done and login page is loaded.
        shows error based on criteria.
    '''
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password_2')
        username = request.POST.get('username')
        if password == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user = CustomUser(username=username, user_type=user_type, first_name=first_name, last_name=last_name, email=email, password=password)
                print("user created")
                user.set_password(password)
                user.is_active = True
                user.save()
                return HttpResponseRedirect('login')
        else:
            messages.info(request, 'password doesn\'t match')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    '''
        authentication check, if true takes to profile,
        if not true shows error message
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print("user", user, username, password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('profile')
        else:
            messages.info(request, 'Invalid credentials. Try again.')
            print("invalid")
            return redirect('login')
    else:
        return render(request, 'login.html')

def profile(request):
    '''
        loads profile based on user type, 
        if not allowed returns to error page
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
        return HttpResponseRedirect('not_allowed')

def not_allowed(request):
    '''
        renders a forbidden page if request not authenticated
    '''
    return render(request, 'not_allowed.html')

def contact(request):
    '''
        renders contact page
    '''
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

def form_save(request):
    '''
        save thesis form data then returns to user (student) profile
        also checks duplicacy
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
            s1_exists_in_1 = compact_Form.objects.filter(student_1_id_id=student_1_id).count()
            s1_exists_in_2 = compact_Form.objects.filter(student_2_id=student_1_id).count()
            s2_exists_in_1 = compact_Form.objects.filter(student_1_id_id=student_2_id).count()
            s2_exists_in_2 = compact_Form.objects.filter(student_2_id=student_2_id).count()
            if s1_exists_in_1:
                compact_Form.objects.get(student_1_id_id=student_1_id).delete()
            elif s1_exists_in_2:
                compact_Form.objects.get(student_2_id=student_1_id).delete()
            elif s2_exists_in_1:
                compact_Form.objects.get(student_1_id_id=student_2_id).delete()
            elif s2_exists_in_2:
                compact_Form.objects.get(student_2_id=student_2_id).delete()

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
        return HttpResponseRedirect('not_allowed')


def form_output(request):
    '''
        shows form output data and assign option
    '''
    if request.user.is_authenticated and request.user.user_type=="admin":
        all_form = compact_Form.objects.all()
        all_teacher = CustomUser.objects.filter(user_type="teacher")
        return render(request,'form_table_admin compact.html', {'all_form': all_form, 'all_teacher': all_teacher})
    else:
        return HttpResponseRedirect('not_allowed')

def filter_form(request):
    '''
        shows form output data based on cgpa filter and assign option
    '''
    if request.user.is_authenticated and request.user.user_type=="admin":
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
        return HttpResponseRedirect('not_allowed')


def tasks(request):
    '''
        shows form. User can fill or update form.
        user can update team member if that user 
        has not yet formed another team
    '''
    if request.user.is_authenticated and request.user.user_type=="student":
        if Student_data.objects.filter(user_id_id=request.user.id).exists():
            user_info = request.user
            teacher_info = CustomUser.objects.filter(user_type="teacher")
            pre_student_info = CustomUser.objects.filter(user_type="student")
            student_info = []
            for x in pre_student_info:
                if x.id != request.user.id and Student_data.objects.filter(user_id_id=x.id).exists():
                    other_team_as_1 = compact_Form.objects.filter(student_1_id_id=x.id).count()
                    other_team_as_2 = compact_Form.objects.filter(student_2_id=x.id).count()
                    print(other_team_as_1, other_team_as_2)
                    if other_team_as_1 != 0:
                        team =  compact_Form.objects.get(student_1_id_id=x.id)
                        if team.student_2_id != request.user.id:
                            continue
                    elif other_team_as_2 != 0:
                        team =  compact_Form.objects.get(student_2_id=x.id)
                        if team.student_1_id_id != request.user.id:
                            continue
                    student_info.append(x)
            user_sd = Student_data.objects.get(user_id_id=request.user.id)
            return render(request, 'thesisform.html', {'user_in': user_info, 
            'user_sd': user_sd, 'all_student': student_info, 'all_teacher': teacher_info})
        else:
            messages.info(request, 'Please update your data first.')
            return HttpResponseRedirect('profile')
        
    else:
        return HttpResponseRedirect('not_allowed')

def filter_user_type(request):
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.user_type=="admin":
            print("here i am")
            user_type = request.POST.get('user_type')
            user_info = request.user
            all_teacher = CustomUser.objects.filter(user_type="teacher")
            all_student = CustomUser.objects.filter(user_type="student")
            td = []
            sd = []
            if user_type == "all":
                return HttpResponseRedirect('search_user')
            elif user_type == "teacher":
                for x in all_teacher:
                    y = None
                    see = Teachers_data.objects.filter(user_id_id=x.id).count()
                    if see != 0:
                        y = Teachers_data.objects.get(user_id_id=x.id)
                    td.append(y)
                return render(request, 'search_user.html', {'user_in': user_info, 'all_teacher': zip(all_teacher,td), 
                'all_student': zip(all_student, sd)})

            elif user_type == "student":
                for x in all_student:
                    y = None
                    see = Student_data.objects.filter(user_id_id=x.id).count()
                    if see != 0:
                        y = Student_data.objects.get(user_id_id=x.id)
                    sd.append(y)
                return render(request, 'search_user.html', {'user_in': user_info, 'all_teacher': zip(all_teacher,td), 
                'all_student': zip(all_student, sd)})

    else:
        return HttpResponseRedirect('not_allowed')

def search_user(request):
    '''
        shows all user profile search
    '''
    if request.user.is_authenticated and request.user.user_type=="admin":
        user_info = request.user
        all_teacher = CustomUser.objects.filter(user_type="teacher")
        all_student = CustomUser.objects.filter(user_type="student")
        td = []
        sd = []
        for x in all_teacher:
            y = None
            see = Teachers_data.objects.filter(user_id_id=x.id).count()
            if see != 0:
                y = Teachers_data.objects.get(user_id_id=x.id)
            td.append(y)
        for x in all_student:
            y = None
            see = Student_data.objects.filter(user_id_id=x.id).count()
            if see != 0:
                y = Student_data.objects.get(user_id_id=x.id)
            sd.append(y)
        return render(request, 'search_user.html', {'user_in': user_info, 'all_teacher': zip(all_teacher,td), 
        'all_student': zip(all_student, sd)})

    else:
        return HttpResponseRedirect('not_allowed')


def search(request):
    '''
        shows teacher profile search
    '''
    if request.user.is_authenticated and request.user.user_type=="student":
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
        return HttpResponseRedirect('not_allowed')

def logout(request):
    '''
        logout
    '''
    auth_logout(request)
    return HttpResponseRedirect('login')

def student_update(request):
    '''
        student data update
    '''
    if request.user.is_authenticated and request.user.user_type=="student":
        user_info = request.user
        x = Student_data.objects.filter(user_id_id=request.user.id).count()
        if x != 0:
            s_id = Student_data.objects.get(user_id_id=request.user.id)
            return render(request, 'student_update.html', {'user_in': user_info, 'user_sd': s_id})
        else:
            return render(request, 'student_update.html', {'user_in': user_info, 'user_sd': user_info})
    else:
        return HttpResponseRedirect('not_allowed')

def student_save(request):
    '''
        student data save
    '''
    if request.user.is_authenticated and request.user.user_type=="student":
        user_info = request.user
        if request.method == 'POST':
            if len(request.FILES) != 0:
                print(request.FILES["photos"])
                photos = request.FILES["photos"]
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
            user = authenticate(request, username=request.user.username, password=password)
            if user is None:
                print("not authenticated, no update")
                messages.info(request, "Password was incorrect. Data was not updated.Try Again.")
                return HttpResponseRedirect('student_update')
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
                if len(request.FILES) != 0:
                    print(request.FILES["photos"])
                    photos = request.FILES["photos"]
                    exist_check.photos=request.FILES["photos"]
                exist_check.save()
            else:        
                st_up = Student_data(mobile_no=mobile_no, user_id_id=user_info.id,
                address=address, blood_group=blood_group, total_cgpa=total_cgpa, 
                major_cgpa=major_cgpa, github=github, linkedin=linkedin)
                if len(request.FILES) != 0:
                    print(request.FILES["photos"])
                    photos = request.FILES["photos"]
                    st_up.photos=request.FILES["photos"]
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
        return HttpResponseRedirect('not_allowed')

def teacher_update(request):
    '''
        teacher data update
    '''
    if request.user.is_authenticated and request.user.user_type=="teacher":
        user_info = request.user
        x = Teachers_data.objects.filter(user_id_id=request.user.id).count()
        if x != 0:
            s_id = Teachers_data.objects.get(user_id_id=request.user.id)
            return render(request, 'teacher_update.html', {'user_in': user_info, 'user_sd': s_id})
        else:
            return render(request, 'teacher_update.html', {'user_in': user_info, 'user_sd': user_info})
    else:
        return HttpResponseRedirect('not_allowed')

def teacher_save(request):
    '''
        teacher data save
    '''
    if request.user.is_authenticated and request.user.user_type=="teacher":
        user_info = request.user
        print(request.method, "teacher up")
        if request.method == 'POST':
            if len(request.FILES) != 0:
                print(request.FILES["photos"])
                photos = request.FILES["photos"]
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
            designation = request.POST.get('designation')
            user = authenticate(request, username=request.user.username, password=password)
            if user is None:
                print("not authenticated, no update")
                messages.info(request, "Password was incorrect. Data was not updated.Try Again.")
                return HttpResponseRedirect('teacher_update')
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
                if len(request.FILES) != 0:
                    print(request.FILES["photos"])
                    photos = request.FILES["photos"]
                    exist_check.photos=request.FILES["photos"]
                exist_check.save()
            else:        
                tc_up = Teachers_data(mobile_no=mobile_no, user_id_id=user_info.id,
                address=address, blood_group=blood_group,  sust_id=sust_id, 
                scholar=scholar, designation=designation)
                if len(request.FILES) != 0:
                    print(request.FILES["photos"])
                    photos = request.FILES["photos"]
                    tc_up.photos=request.FILES["photos"]
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
        return HttpResponseRedirect('not_allowed')


def see_teacher(request, id):
    '''
        students and admins can see the requested teacher profile
    '''
    if request.user.is_authenticated and request.user.user_type=="student":
        user_info = request.user
        teacher = CustomUser.objects.get(id=id)
        td = None
        x = Teachers_data.objects.filter(user_id_id=teacher.id).count()
        if x != 0:
            td = Teachers_data.objects.get(user_id_id=teacher.id)
        return render(request, 'see_teacher.html', {'user_in': teacher, 'user_sd': td})

    elif request.user.is_authenticated and request.user.user_type=="admin":
        user_info = request.user
        teacher = CustomUser.objects.get(id=id)
        td = None
        x = Teachers_data.objects.filter(user_id_id=teacher.id).count()
        if x != 0:
            td = Teachers_data.objects.get(user_id_id=teacher.id)
        return render(request, 'see_teacher.html', {'user_in': teacher, 'user_sd': td})

    else:
        return HttpResponseRedirect('not_allowed')

def see_student(request, id):
    '''
        admins can see the requested student profile
    '''
    if request.user.is_authenticated and request.user.user_type=="admin":
        user_info = request.user
        student = CustomUser.objects.get(id=id)
        sd = None
        x = Student_data.objects.filter(user_id_id=student.id).count()
        if x != 0:
            sd = Student_data.objects.get(user_id_id=student.id)
        return render(request, 'see_student.html', {'user_in': student, 'user_sd': sd})

    else:
        return HttpResponseRedirect('not_allowed')

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
                return render(request, 'login.html')
            sup = CustomUser.objects.get(id=assigned_supervisor_id)
            assigned_supervisor = sup.username
            form_record.assigned_supervisor_id = assigned_supervisor_id
            form_record.assigned_course = assigned_course
            form_record.assigned_external = assigned_external
            form_record.assigned_supervisor = assigned_supervisor
            form_record.action = "Assigned"
            form_record.save()
            return redirect('form_output')
    else:
        return HttpResponseRedirect('not_allowed')

# def plot_show(request):
#     all_form = Form.objects.all()
#     all_teacher = CustomUser.objects.filter(user_type="teacher")
#     user_info = request.user
#     return render(request, 'plot_show.html', {'user_in': user_info, 'all_form': all_form, 'all_teacher': all_teacher})


def pie_chart(request):
    if request.user.is_authenticated and request.user.user_type=="admin":
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
    else:
        return HttpResponseRedirect('not_allowed')



def line_chart(request):
    data=[]
    labels=["Major_CGPA >= 3.5 ", "Total_CGPA >= 3.5","Both_CGPA >= 3.5", "Both_CGPA <= 2"]
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
    if request.user.is_authenticated and request.user.user_type=="admin":
        return render(request, 'home1.html')
    else:
        return HttpResponseRedirect('not_allowed')  

class NoticeListView(ListView):
    model = Notice   
    template_name='notice_view.html'
    context_object_name='notices'
    ordering=['-created_at']


class NoticeCreateView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Notice
    #invoke blog/post_create.html   <app_name>/ <model_name>_<ViewType>.html
    fields = ['title','message']
    template_name='notice_form.html'
    login_url='/'
    success_message = "Notice is Created Successfully"

    def form_valid(self, form):
        form.instance.created_by= self.request.user
        return super().form_valid(form)


class NoticeDetailView(DetailView):
    model = Notice
    template_name='notice_detail.html'

    #invoke blog/post_detail.html   <app_name>/ <model_name>_<ViewType>.html