from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *

from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin


#____________________________Registation & Login & Logout_____________________________
class Owner_Registation(View):
    def get(self,request):
        form = RegistationForm()

        content = {"form":form}
        return render(request,'account/signup_owner.html',content)

    def post(self,request,*args,**kwargs):
        form = RegistationForm(request.POST or None )

        if form.is_valid():
            a = form.save()
            group = Group.objects.get(name='owner')
            a.groups.add(group)
            return redirect('login')
        else:
            return redirect('owner_signup')




class User_Registaion(View):
    def get(self,request):
        form = RegistationForm()
        data = {"form":form}
        return render(request, 'account/signup_user.html', data)

    def post(self,request,*args,**kwargs):
        f = RegistationForm(request.POST or None)

        if f.is_valid():
            c = f.save()
            group = Group.objects.get(name='emplyee')
            c.groups.add(group)
            return redirect('login')
        else:
            return redirect('signup')


class Login(View):
    def get(self,request):

        return render(request,'account/login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email)
            user = authenticate(username=username.username, password=password)
        except:
            return redirect('login')

        try:
            if user is not None:
                login(request, user)
            else:
                return redirect('login')

            if user.groups.filter(name="emplyee").exists():
                return redirect('joblist')
            elif user.groups.filter(name='owner').exists():
                data = CompanyeeDetails.objects.filter(user=user).count()
                if (data == 1):
                    return redirect('owner_profile')
                else:
                    return redirect('addcompanydetail')
            else:
                return redirect('login')

        except user.DoesNotExist:
            return redirect('login')


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')
        return render(request,'user/home.html')


#_______________________________________ Home jobList   & Detail  ____________________________


class Home(ListView):
    model = Jobs
    context_object_name = 'jonlist'
    template_name = 'account/home.html'


class JobDetail(DetailView):
    model = Jobs
    context_object_name = 'detail_job'
    template_name = 'account/jobdetail.html'



class Search(View):
    def get(self,request):
        search = request.GET.get('search')
        data = Jobs.objects.filter(job_name__icontains = search)
        context = {"jonlist":data}
        return render(request,'account/home.html',context)




#####################################            Owner Work       #################################################


class AddcompanyDetail(LoginRequiredMixin,View):
    def get(self,request):
        form = CompanyDetailForms()
        data = {"form":form}
        return render(request,'owner/add_company.html',data)

    def post(self,request,*args,**kwargs):
        form = CompanyDetailForms(request.POST or None , request.FILES or None)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('owner_profile')


class OwnerProfile(LoginRequiredMixin,View):
    def get(self,request):
        data = {"owner_profile":CompanyeeDetails.objects.get(user=request.user)}

        return render(request,'owner/profile.html',data)


class AddJobs(LoginRequiredMixin,View):
    def get(self,request):
        context = {"form":AddJobsForms()}
        return render(request,'owner/add_job.html',context)


    def post(self,request,*args,**kwargs):
        form = AddJobsForms(request.POST or None)
        com_id = CompanyeeDetails.objects.get(user=request.user).com_id

        if form.is_valid():
            f = form.save(commit=False)
            f.com_id = CompanyeeDetails(com_id)
            f.save()
            return redirect('alljob')



class AllJobs(LoginRequiredMixin,View):
    def get(self,request):
        data = {"alljob":Jobs.objects.filter(com_id__user = request.user)}

        return render(request,'owner/all_job.html',data)



class AllApplyJob(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        data = {"applyforjob":Apply.objects.filter(job_id__com_id__user = request.user , status=False)}

        return render(request,'owner/all_apply.html',data)


class SelectForInterView(LoginRequiredMixin,View):
    def get(self,request,pk):
        st = Apply.objects.get(apply_id = pk)
        st.status = True
        st.save()
        return redirect('allapplyforjob')



class AllSelectedForInterView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        data = {"allselectedforinterview":Apply.objects.filter(job_id__com_id__user = request.user , status=True)}

        return render(request,'owner/allselectedforinterview.html',data)



class UpdateCompanyDetail(LoginRequiredMixin,UpdateView):
    model = CompanyeeDetails
    form_class = CompanyDetailForms
    template_name = 'owner/company_detail_update.html'

    def form_valid(self, form):
        form.save()
        return redirect('owner_profile')


class DeleteJob(LoginRequiredMixin,View):
    def get(self,request,pk):
        data = Jobs.objects.get(job_id = pk)
        data.delete()
        return redirect('alljob')




#------------------------------------------ User --------------------------------------


class HomeUser(LoginRequiredMixin,ListView):
    model = Jobs
    context_object_name = 'joblist'
    template_name = 'user/home.html'


class JobDetailUser(LoginRequiredMixin,DetailView):
    model = Jobs
    context_object_name = 'detail_job'
    template_name = 'user/job_detail.html'


class SearchJobUser(LoginRequiredMixin,View):
    def get(self,request):
        search = request.GET.get('search')
        data = Jobs.objects.filter(job_name__icontains = search)
        context = {"joblist":data}
        return render(request,'user/home.html',context)




class ApplyForJob(LoginRequiredMixin,View):
    def get(self,request,pk,*args,**kwargs):
        form = ApplyForms()
        context = {"form":form,"pk":pk}
        return render(request,'user/apply_job.html',context)

    def post(self,request,pk,*args,**kwargs):
        form = ApplyForms(request.POST or None ,request.FILES or None)

        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.job_id = Jobs(pk)
            a.save()
            return redirect('joblist')
        return render(request,'user/apply_job.html')


class MyAllApply(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        context = {"myallaply":Apply.objects.filter(user = request.user)}
        return render(request, 'user/my_all_apply.html', context)


class MySelectedApply(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        data = {"myselectedapply":Apply.objects.filter(user=request.user , status=True)}
        return render(request, 'user/myselectedapply.html', data)


class MyPandingApply(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        data = {"mypandingapply":Apply.objects.filter(user=request.user , status=False)}
        return render(request,'user/mypandingapply.html',data)



class MyApplyDetail(LoginRequiredMixin,DetailView):
    model = Apply
    context_object_name = 'detail_job'
    template_name = 'user/myapplydetail.html'










