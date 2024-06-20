from django.shortcuts import render, redirect, get_object_or_404
from . models import UserLogin, AdminLogin, UserProfile, AdminProfile, Events, Manage, Notice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse



def homepage(request):
    data4 = Events.objects.all()
    data3 = UserProfile.objects.all()
    context = {
        'data4': data4,
        'data3': data3,
    }
    return render(request, 'homepage.html', context)  

def memberlogin(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        try:
            user = UserLogin.objects.get(username=username1)
            if user.password == password1:
                request.session['username'] = username1  # Set session variable
                return redirect('memberpage')
            else:
                error_message = "Incorrect password. Please try again."
        except UserLogin.DoesNotExist:
            error_message = "Username does not exist. Please try again."

        return render(request, "memberlogin.html", {"error_message": error_message})
    return render(request, 'memberlogin.html')

def application(request):
    if request.method == 'POST':
        name1 = request.POST['name']
        studID1 = request.POST['studID']
        birth_date1 = request.POST['birth_date']
        email1 = request.POST['email']
        phonenum1 = request.POST['phonenum']
        gender1 = request.POST['gender']
        icnum1 = request.POST['icnum']
        course1 = request.POST['course']
        semester1 = request.POST['semester']
        address1 = request.POST['address']
        reason1 = request.POST['reason']

        result_Main_Img = request.FILES.get('result_Main_Img', None)
        pfp_Main_Img = request.FILES.get('pfp_Main_Img', None)

        Stud = UserProfile(
            name=name1,
            studID=studID1,
            birth_date=birth_date1,
            email=email1,
            phonenum=phonenum1,
            gender=gender1,
            icnum=icnum1,
            course=course1,
            semester=semester1,
            address=address1,
            reason=reason1,
            pfp_Main_Img=pfp_Main_Img,
            result_Main_Img=result_Main_Img
        )
        Stud.save()

        context2 = {
            'message2': 'Application sent',
        }
        return render(request, 'application.html', context2)
    else:
        dict2 = {
            'message2': ''
        }
    return render(request, "application.html", dict2)

def memberpage(request):
    if 'username' in request.session:
        username = request.session['username']
        user = get_object_or_404(UserProfile, name=username)
        context = {
            'user': user,
        }
        return render(request, "memberpage.html", context)
    else:
        return redirect('memberlogin')

def memberevent(request):
    data4 = Events.objects.all()
    context6 = {
        'data4':data4
    }
    return render (request, "memberevent.html", context6)

def memberboard(request):
    data = Notice.objects.all()
    context6 = {
        'data':data
    }
    return render (request,'memberboard.html', context6)

def aboutus(request):
    return render (request, 'aboutus.html')

def events(request):
    return render (request, 'events.html')

def member(request):
    data3 = UserProfile.objects.all()
    context6 = {
        'data3':data3
    }    
    return render (request, 'member.html', context6)

def adminlogin(request):
    if request.method == "POST":
        username2 = request.POST['username1']
        password2 = request.POST['password1']

        try :
            user = AdminLogin.objects.get(username1=username2)
            if user.password1 == password2:
                return redirect('adminprofile')
            else:
                error_message = "Incorrect password. Please try again."
        except AdminLogin.DoesNotExist:
            error_message = "Username does not exist. Please try again."

        return render(request, "adminlogin.html", {"error_message" : error_message})
    
    return render (request, 'adminlogin.html')

def adminprofile(request):
    if request.method == 'POST':
        name2 = request.POST['name1']
        email2 = request.POST['email1']
        address2 = request.POST['address1']
        lectID1 = request.POST['lectID']
        phonenum2 = request.POST['phonenum1']
        icnum2 = request.POST['icnum1']

        if request.FILES:
            pfp1_Main_Img = request.FILES['pfp1_Main_Img']
        else:
            pfp1_Main_Img = None

        Lect = AdminProfile(name1=name2, email1=email2, address1=address2, lectID=lectID1, 
                            phonenum1=phonenum2, icnum1=icnum2, pfp1_Main_Img=pfp1_Main_Img)
        Lect.save()

        context3 = {
            'message3': 'Profile created',
        }
        return render(request, 'adminprofile.html', context3)
    else:
        dict3 = {
            'message3': 'Profile not created yet'
        }
        return render(request, "adminprofile.html", dict3)
    
def adminprofiledisplay(request):
    data2 = AdminProfile.objects.all()
    context8 = {
        'data2':data2
    }
    return render(request, "adminprofiledisplay.html", context8)

def adminprofiledisplay1(request):
    return render(request, 'adminprofiledisplay.html')

def adminprofileupdate(request, id):
    x = get_object_or_404(AdminProfile, lectID=id)
    dict6 = {
        'x': x
    }
    return render(request, "adminprofileupdate.html", dict6)

def adminprofileupdate_data(request, id):
    name2 = request.POST.get('name1')
    email2 = request.POST.get('email1')
    address2 = request.POST.get('address1')
    lectID1 = request.POST.get('lectID')
    phonenum2 = request.POST.get('phonenum1')
    icnum2 = request.POST.get('icnum1')
    pfp1_Main_Img = request.FILES.get('pfp1_Main_Img')

    data = get_object_or_404(AdminProfile, lectID=id)
    data.name1 = name2
    data.email1 = email2
    data.address1 = address2
    data.lectID = lectID1
    data.phonenum1 = phonenum2
    data.icnum1 = icnum2
    if pfp1_Main_Img:
        data.pfp1_Main_Img = pfp1_Main_Img
    data.save()
    return HttpResponseRedirect(reverse("adminprofiledisplay"))

def adminprofile1(request):
    return render(request, 'adminprofile.html')

def adminprofiledelete(request,id):
    x = get_object_or_404(AdminProfile, lectID=id)
    dict7 = {
        'x': x
    }
    return render(request, "adminprofiledelete.html", dict7)

def adminprofiledelete_data(request,id):
    data = get_object_or_404(AdminProfile, lectID=id)
    data.delete()
    return HttpResponseRedirect(reverse("adminprofile"))  

def adminapproval(request):
    data1 = UserProfile.objects.all()
    context7 = {
        'data1':data1
    }
    return render(request, 'adminapproval.html', context7)

def adminapproval1(request):
    return render (request, 'adminapproval.html')

def adminapprovaldelete(request,id):
    x = get_object_or_404(UserProfile, studID=id)
    dict8 = {
        'x': x
    }
    return render(request, "adminapprovaldelete.html", dict8)

def adminapprovaldelete_data(request,id):
    data = get_object_or_404(UserProfile, studID=id)
    data.delete()
    return HttpResponseRedirect(reverse("adminapproval")) 

def adminevent(request):
    if request.method == 'POST':
        eventname1 = request.POST['eventname']
        date1 = request.POST['date']
        time1 = request.POST['time']
        venue1 = request.POST['venue']

        if request.FILES:
            event_Main_Img = request.FILES['event_Main_Img']
        else:
            event_Main_Img = None

        Act = Events(eventname=eventname1, date=date1, time=time1, venue=venue1, event_Main_Img=event_Main_Img)
        Act.save()

        context4 = {
            'message4': 'Event uploaded',
        }
        return render(request, 'adminevent.html', context4)
    else:
        dict4 = {
            'message4': ''
        }
        return render(request, "adminevent.html", dict4)
    
def admineventdisplay(request):
    data4 = Events.objects.all()
    context6 = {
        'data4':data4
    }
    return render(request, 'admineventdisplay.html', context6)

def admineventdisplay1(request):
     return render(request, 'admineventdisplay.html')

def admineventupdate(request, id):
    x = get_object_or_404(Events, eventname=id)
    dict8 = {
        'x': x
    }
    return render(request, "admineventupdate.html", dict8)

def admineventupdate_data(request, id):
    eventname1 = request.POST.get('eventname')
    date1 = request.POST.get('date')
    time1 = request.POST.get('time')
    venue1 = request.POST.get('venue')
    event_Main_Img = request.FILES.get('event_Main_Img')

    data = get_object_or_404(Events, eventname=id)
    data.eventname = eventname1
    data.date = date1
    data.time = time1
    data.venue = venue1
    if event_Main_Img:
        data.event_Main_Img = event_Main_Img
    data.save()
    return HttpResponseRedirect(reverse("admineventdisplay"))

def adminevent1(request):
    return render(request, "adminevent.html")

def admineventdelete(request,id):
    x = get_object_or_404(Events, eventname=id)
    dict9 = {
        'x': x
    }
    return render(request, "admineventdelete.html", dict9)

def admineventdelete_data(request,id):
    data = get_object_or_404(Events, eventname=id)
    data.delete()
    return HttpResponseRedirect(reverse("adminevent")) 

def adminboard(request):
    if request.method=='POST':
        title1 = request.POST['title']
        content1 = request.POST['content']
        Board = Notice(title=title1, content=content1)
        Board.save()

        context5 = {
            'message5':'Notice has been sent to members'
        }
        return render(request, 'adminboard.html', context5)

    else :
        dict5 = {
            'message5':''
        }
    return render (request,'adminboard.html',dict5)

def adminboarddisplay(request):
    data = Notice.objects.all()
    context6 = {
        'data':data
    }
    return render(request, 'adminboarddisplay.html', context6)

def adminboard1(request):
    return render(request, "adminboard.html")

def adminboarddelete(request,id):
    x = get_object_or_404(Notice, title=id)
    dict12 = {
        'x': x
    }
    return render(request, "adminboarddelete.html", dict12)

def adminboarddelete_data(request,id):
    data = get_object_or_404(Notice, title=id)
    data.delete()
    return HttpResponseRedirect(reverse("adminboard")) 

def adminmember(request):
    data11 = UserProfile.objects.all()
    selected_user = None
    user_name = None

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        if user_name:
            selected_user = get_object_or_404(UserProfile, name=user_name)
    
    # Assuming you have a form for selecting position
    # Process the form data
    if 'position' in request.POST:
        position = request.POST['position']
        if selected_user:
            selected_user.positions.create(memposition=position)
            # Redirect to memberpage after updating position
            return redirect('memberpage')

    context11 = {
        'data11': data11,
        'selected_user': selected_user,
        'user_name': user_name
    }
    return render(request, 'adminmember.html', context11)

def adminmemberupdate(request):
    user_name = request.GET.get('user_name') or request.POST.get('user_name')
    if request.method == 'POST':
        memposition1 = request.POST.get('memposition')
        selected_user = get_object_or_404(UserProfile, name=user_name)

        position, created = Manage.objects.get_or_create(user=selected_user)
        position.memposition = memposition1
        position.save()

        data11 = UserProfile.objects.all()
        context1 = {
            'message': 'You have assigned the position',
            'data11': data11,
            'selected_user': selected_user,
            'user_name': user_name
        }
        return render(request, 'adminmember.html', context1)
    else:
        context1 = {
            'message': 'Not assigned yet',
            'user_name': user_name
        }
        return render(request, 'adminmemberupdate.html', context1)
    
def adminmemberdelete(request):
    if request.method == 'GET':
        user_name = request.GET.get('user_name')
        user = get_object_or_404(UserProfile, name=user_name)
        return render(request, 'adminmemberdelete.html', {'user_name': user_name})

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user = get_object_or_404(UserProfile, name=user_name)
        Manage.objects.filter(user=user).delete()  # Delete related Manage objects
        user.delete()  # Delete UserProfile
        return redirect('adminmember')

    return redirect('adminmember')  # Redirect to adminmember if no user_name found in GET or POST
    
def createuserpass(request, user_name):
    user = get_object_or_404(UserProfile, name=user_name)
    user_profile = UserLogin.objects.filter(username=user_name).first()

    if request.method == 'POST':
        password = request.POST.get('password')
        if user_profile is None:
            UserLogin.objects.create(username=user_name, password=password)
        else:
            user_profile.password = password
            user_profile.save()
        return render(request, 'createuserpass.html', {'user': user, 'message': 'New account created'})
    
    return render(request, 'createuserpass.html', {'user': user, 'user_profile': user_profile})