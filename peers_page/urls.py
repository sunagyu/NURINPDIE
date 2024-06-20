from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("MemberLogin/", views.memberlogin, name="memberlogin"),
    path("OnlineApplication/", views.application, name="application"),
    path("MemberPage/", views.memberpage, name="memberpage"),
    path("MemberEvent/", views.memberevent, name="memberevent"),
    path("MemberBoard/", views.memberboard, name="memberboard"),
    path("AboutUs/", views.aboutus, name="aboutus"),
    path("Events/", views.events, name="events"),
    path("Member/", views.member, name="member"),
    path("AdminLogin/", views.adminlogin, name="adminlogin"),
    path("AdminProfile/", views.adminprofile, name="adminprofile"),
    path("displayAdminProfile/", views.adminprofiledisplay, name="adminprofiledisplay"),
    path("adminprofileupdate/<str:id>", views.adminprofileupdate, name="adminprofileupdate"),
    path("adminprofileupdate/adminprofileupdate_data/<str:id>", views.adminprofileupdate_data, name="adminprofileupdate_data"),
    path("adminprofiledelete/<str:id>", views.adminprofiledelete, name="adminprofiledelete"),
    path("adminprofiledelete/adminprofiledelete_data/<str:id>", views.adminprofiledelete_data, name="adminprofiledelete_data"),
    path("adminapprovaldelete/<str:id>", views.adminapprovaldelete, name="adminapprovaldelete"),
    path("adminapprovaldelete/adminapprovaldelete_data/<str:id>", views.adminapprovaldelete_data, name="adminapprovaldelete_data"),
    path("AdminApproval/", views.adminapproval, name="adminapproval"),
    path("AdminEvent/", views.adminevent, name="adminevent"),
    path("displayAdminEvent/", views.admineventdisplay, name="admineventdisplay"),
    path("admineventupdate/<str:id>", views.admineventupdate, name="admineventupdate"),
    path("admineventupdate/admineventupdate_data/<str:id>", views.admineventupdate_data, name="admineventupdate_data"),
    path("admineventdelete/<str:id>", views.admineventdelete, name="admineventdelete"),
    path("admineventdelete/admineventdelete_data/<str:id>", views.admineventdelete_data, name="admineventdelete_data"),
    path("AdminBoard/", views.adminboard, name="adminboard"),
    path('displayNoticeAdmin/', views.adminboarddisplay, name='adminboarddisplay'),
    path("adminboarddelete/<str:id>", views.adminboarddelete, name="adminboarddelete"),
    path("adminboarddelete/adminboarddelete_data/<str:id>", views.adminboarddelete_data, name="adminboarddelete_data"),
    path("AdminMember/", views.adminmember, name="adminmember"),
    path("AdminCreateUserPass/<str:user_name>/", views.createuserpass, name="createuserpass"),
    path("AdminAssignPosition/", views.adminmemberupdate, name="adminmemberupdate"),
    path("adminmemberdelete/", views.adminmemberdelete, name="adminmemberdelete"),
]
