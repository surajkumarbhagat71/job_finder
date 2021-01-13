from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    #-------------------------Registation & Login & Logout----------------------#

    path('usersignup',User_Registaion.as_view(),name="usersignup"),
    path('ownersingup',Owner_Registation.as_view(),name="owner_signup"),
    path('login/',Login.as_view(),name="login"),
    path('logout',Logout.as_view(),name="logout"),


    ################## Home & detail ################

    path('',Home.as_view(),name="home"),
    path('jobdetail/<int:pk>',JobDetail.as_view(),name='jobdetail'),
    path('search', Search.as_view(), name="search"),

    #---------------------------------------------- Owner ---------------------------------------#

    path('addcompanydetail',AddcompanyDetail.as_view(),name='addcompanydetail'),
    path('owner_profile',OwnerProfile.as_view(),name="owner_profile"),
    path('addjob',AddJobs.as_view(),name="add_job"),
    path('alljob',AllJobs.as_view(),name="alljob"),
    path('allaplyforjob',AllApplyJob.as_view(),name="allapplyforjob"),
    path('selectforinterview/<int:pk>',SelectForInterView.as_view(),name="selectforinterview"),
    path('allselectedforinterview',AllSelectedForInterView.as_view(),name='allselectedforinterview'),
    path('company_detail_update/<int:pk>',UpdateCompanyDetail.as_view(),name='company_detail_update'),
    path('delete_job/<int:pk>',DeleteJob.as_view(),name='delete_job'),



    ############################   user #####################################################

    path('apply/<int:pk>',ApplyForJob.as_view(),name="apply"),
    path('joblist',HomeUser.as_view(),name="joblist"),
    path('jobdetailuser/<int:pk>',JobDetailUser.as_view(),name="jobdetailuser"),
    path('userjobsearch',SearchJobUser.as_view(),name="searchjobuser"),
    path('detail_job/<int:pk>', MyApplyDetail.as_view(), name="my_apply_detail"),
    path('myselectedapply', MySelectedApply.as_view(), name="myselectedapply"),
    path('mypandingapply', MyPandingApply.as_view(), name="mypandingapply"),
    path('myallapply', MyAllApply.as_view(), name="myallapply"),



    #########################################################################

    path('password_reset/',auth_views.PasswordResetView.as_view(),name = 'password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),




]

