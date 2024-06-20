from django.db import models

class UserLogin(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100)

class AdminLogin(models.Model):
    username1 = models.CharField(max_length=50, primary_key=True)
    password1 = models.CharField(max_length=100)

class UserProfile(models.Model):
    name = models.TextField(max_length=100, primary_key=True)
    studID = models.CharField(max_length=70)
    birth_date = models.CharField(max_length=10,blank=True)
    email = models.CharField(max_length=128)
    phonenum = models.CharField(max_length=40)
    gender = models.TextField(max_length=10)
    icnum = models.CharField(max_length=40)
    course = models.TextField(max_length=100)
    semester = models.IntegerField()
    address = models.CharField(max_length=200)
    reason = models.TextField(max_length=400)
    result_Main_Img = models.ImageField(upload_to='images/')
    pfp_Main_Img = models.ImageField(upload_to='images/')
    filled_at = models.DateTimeField(auto_now_add=True)

class AdminProfile(models.Model):
    name1 = models.TextField(max_length=100)
    email1 = models.CharField(max_length=128)
    address1 = models.CharField(max_length=200)
    lectID = models.CharField(max_length=70, primary_key=True)    
    phonenum1 = models.CharField(max_length=40)
    icnum1 = models.CharField(max_length=40)
    pfp1_Main_Img = models.ImageField(upload_to='images/')

class Events(models.Model):
    eventname = models.CharField(max_length=128)
    date = models.DateField(max_length=10)
    time = models.TimeField(max_length=40)
    venue = models.CharField(max_length=50)
    post_at = models.DateTimeField(auto_now_add=True)
    event_Main_Img = models.ImageField(upload_to='images/')

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)

class Manage(models.Model):
    memposition = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='positions')