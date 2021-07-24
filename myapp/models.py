from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from markdown import markdown
from django.urls import reverse
# Create your models here.
#Lets build model classes here.
class CustomUser(AbstractUser):
    user_type = models.CharField(null=True, blank=True, default=None, max_length=55)
    first_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    last_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    email = models.CharField(null=True, blank=True, default=None, max_length=55)
    password = models.CharField(null=True, blank=True, default=None, max_length=55)
    password1 = models.CharField(null=True, blank=True, default=None, max_length=55)

    def __str__(self):
        return self.email

class Student_data(models.Model):
    user_id = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    # student_id = models.AutoField(null=False,blank=False,default=None,primary_key=True)
    date_of_birth = models.DateField(null=True,blank=True,default=None)
    #reg_no = models.CharField(null=True,blank=True,default=None,max_length=20) ##
    address = models.TextField(null=True,blank=True,default=None)
    gender = models.CharField(null=True,blank=True,default=None,max_length=20)
    mobile_no = models.CharField(null=True,blank=True,default=None,max_length=20)
    blood_group = models.CharField(null=True,blank=True,default=None,max_length=20)
    photos = models.FileField(null=True,blank=True,default="images/default.png",upload_to='images/')
    major_cgpa = models.FloatField(null=True,blank=True,default=0.0,max_length=5)
    total_cgpa = models.FloatField(null=True,blank=True,default=0.0,max_length=5)
    linkedin = models.CharField(null=True, blank=True, default=None, max_length=55)
    github = models.CharField(null=True, blank=True, default=None, max_length=55)


class Teachers_data(models.Model):
    #teacher_id = models.AutoField(null=False,blank=False,default=None,primary_key=True)
    user_id = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True,blank=True,default=None)
    gender = models.CharField(null=True,blank=True,default=None,max_length=20)
    address = models.TextField(null=True, blank=True, default=None)
    blood_group = models.CharField(null=True,blank=True,default=None,max_length=20)
    mobile_no = models.CharField(null=True,blank=True,default=None,max_length=20)
    designation = models.TextField(null=True,blank=True,default=None)
    photos = models.FileField(null=True,blank=True,default="teacher/default.png",upload_to='teacher/')
    sust_id = models.CharField(null=True, blank=True, default=None, max_length=55)
    scholar = models.CharField(null=True, blank=True, default=None, max_length=55)

class Teacher_edu(models.Model):
    # edu_id=models.AutoField(null=False,blank=False,default=None,primary_key=True)
    user_id = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    MSc_Institute_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    MSc_Institute_Country = models.CharField(null=True, blank=True, default=None, max_length=55)
    MSc_start_date = models.CharField(null=True, blank=True, default=None, max_length=55)
    MSc_end_date = models.CharField(null=True, blank=True, default=None, max_length=55)

    Phd_Institute_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    Phd_Institute_Country = models.CharField(null=True, blank=True, default=None, max_length=55)
    Phd_start_date = models.CharField(null=True, blank=True, default=None, max_length=55)
    Phd_end_date = models.CharField(null=True, blank=True, default=None, max_length=55)

    
class Paper(models.Model):
    # paper_id=models.AutoField(null=False,blank=False,default=None,primary_key=True)
    user_id = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    Research_area = models.CharField(null=True, blank=True, default=None, max_length=55)
    Published_Paper = models.CharField(null=True, blank=True, default=None, max_length=55)
    Published_Journal = models.CharField(null=True, blank=True, default=None, max_length=55)


class compact_Form(models.Model):
    # paper_id=models.AutoField(null=False,blank=False,default=None,primary_key=True)
    student_1_id = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    student_1_username = models.CharField(null=True, blank=True, default=None, max_length=55)
    student_1_majorcg =  models.FloatField(null=True,blank=True,default=None,max_length=5)
    student_1_totalcg =  models.FloatField(null=True,blank=True,default=None,max_length=5)
    student_1_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    student_2_id = models.CharField(null=True, blank=True, default=None, max_length=55)
    student_2_username = models.CharField(null=True, blank=True, default=None, max_length=55)
    student_2_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    student_2_majorcg =  models.FloatField(null=True,blank=True,default=None,max_length=5)
    student_2_totalcg =  models.FloatField(null=True,blank=True,default=None,max_length=5)
    Course = models.CharField(null=True, blank=True, default=None, max_length=55)
    topic = models.CharField(null=True, blank=True, default=None, max_length=500)
    description = models.CharField(null=True, blank=True, default=None, max_length=5000)
    supervisor_1 = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_2 = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_3 = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_4 = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_5 = models.CharField(null=True, blank=True, default=None, max_length=55)
    external = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_1_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_2_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_3_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_4_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    supervisor_5_name = models.CharField(null=True, blank=True, default=None, max_length=55)
    assigned_external = models.CharField(null=True, blank=True, default=None, max_length=55)
    assigned_course = models.CharField(null=True, blank=True, default=None, max_length=55)
    assigned_supervisor = models.CharField(null=True, blank=True, default=None, max_length=55)
    assigned_supervisor_id = models.CharField(null=True, blank=True, default=None, max_length=55)
    action = models.CharField(null=True, blank=True, default="Save", max_length=55)

class Notice(models.Model):
	title = models.CharField(max_length=100)
	message = models.TextField(max_length=2000)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.DO_NOTHING)
    
	def __str__(self):
		return self.title
        
	def get_message_as_markdown(self):
		return mark_safe(markdown(self.message))       

	def get_absolute_url(self):
		return  reverse('notice-detail',kwargs={'pk':self.pk})