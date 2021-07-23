# Generated by Django 3.0.5 on 2021-07-20 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_form_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='compact_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_1_majorcg', models.FloatField(blank=True, default=None, max_length=5, null=True)),
                ('student_1_totalcg', models.FloatField(blank=True, default=None, max_length=5, null=True)),
                ('student_1_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('student_2_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('student_2_majorcg', models.FloatField(blank=True, default=None, max_length=5, null=True)),
                ('student_2_totalcg', models.FloatField(blank=True, default=None, max_length=5, null=True)),
                ('student_2_username', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('Course', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('topic', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('description', models.CharField(blank=True, default=None, max_length=5000, null=True)),
                ('supervisor_1', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_2', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_3', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_4', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_5', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('external', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_1_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_2_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_3_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_4_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('supervisor_5_name', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('assigned_external', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('assigned_course', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('assigned_supervisor', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('assigned_supervisor_id', models.CharField(blank=True, default=None, max_length=55, null=True)),
                ('action', models.CharField(blank=True, default='Save', max_length=55, null=True)),
                ('student_1_username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]