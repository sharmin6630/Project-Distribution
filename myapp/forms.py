from django import forms
from .models import *
  
class StudentForm(forms.ModelForm):
  
    class Meta:
        model = Student_data
        fields = ['date_of_birth', 'address', 'gender', 'mobile_no', 'blood_group', 
        'photos', 'major_cgpa', 'total_cgpa', 'linkedin', 'github']

# def student_save(request):
#     user_info = request.user
#     print(request.method, "hihi")
#     if request.method == 'POST':
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             password = request.POST.get('password')
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             email = request.POST.get('email')
#             new_password = request.POST.get('new_password')
#             mobile_no = form.cleaned_data['mobile_no']
#             blood_group = form.cleaned_data['blood_group']
#             address = form.cleaned_data['address']
#             total_cgpa = form.cleaned_data['total_cgpa']
#             major_cgpa = form.cleaned_data['major_cgpa']
#             github = form.cleaned_data['github']
#             linkedin = form.cleaned_data['linkedin']
#             photos = form.cleaned_data['photos']
#             user = authenticate(request, username=request.user.username, password=password)
#             if user is None:
#                 print("not authenticated")
#                 return render(request, 'profile_student.html', {'user_in': request.user})
#             x = Student_data.objects.filter(user_id_id=request.user.id).count()
#             if x != 0:
#                 exist_check = Student_data.objects.get(user_id_id=request.user.id)
#                 exist_check.mobile_no=mobile_no
#                 exist_check.user_id_id=user_info.id
#                 exist_check.address=address
#                 exist_check.blood_group=blood_group
#                 exist_check.total_cgpa=total_cgpa 
#                 exist_check.major_cgpa=major_cgpa 
#                 exist_check.github=github
#                 exist_check.linkedin=linkedin
#                 exist_check.photos=photos
#                 exist_check.save()
#             else:        
#                 st_up = Student_data(mobile_no=mobile_no, user_id_id=user_info.id,
#                 address=address, blood_group=blood_group, total_cgpa=total_cgpa, 
#                 major_cgpa=major_cgpa, github=github, linkedin=linkedin, photos=photos)
#                 st_up.save()
#             user_info = CustomUser.objects.get(id=request.user.id)
#             user_info.first_name=first_name
#             user_info.last_name=last_name
#             user_info.email=email
#             if len(new_password) != 0:
#                 print("user password updated")
#                 user_info.set_password(new_password)
#             user_info.is_active = True
#             user_info.save()
#             if x != 0:
#                 s_id = Student_data.objects.get(user_id_id=request.user.id)
#                 return render(request, 'profile_student.html', {'user_in': user_info, 'user_sd': s_id})
#             else:
#                 return render(request, 'profile_student.html', {'user_in': user_info, 'user_sd': user_info})
#         else:
#             return render(request,'home.html')

#     return render(request, 'home.html')

