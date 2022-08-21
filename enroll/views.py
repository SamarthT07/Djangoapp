from django.shortcuts import render
from .forms import signupform, edituserform, editadminform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.
def sign(request):
    if request.method=="POST":
        fm=signupform(request.POST)
        email=request.POST['email']
        send_mail(
            'hello',
            'this mail ',
            'shridhar.jadhav2003@gmail.com',
            [ email],
        )
        print(email)
        if fm.is_valid():

            fm.save()
            messages.success(request,'data saved succcessfully')
    else:
        fm=signupform()
    return render(request,'enroll/signup.html',{'form':fm})
def ulogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']

                user=authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')


        else:
            fm=AuthenticationForm()
        return render(request,'enroll/login.html',{'form1':fm})
    else:
        return HttpResponseRedirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser== True:
                fm=editadminform(request.POST,instance=request.user)
                abc=User.objects.all()
            else:
                fm=edituserform(request.POST,instance=request.user)
                abc=None
            if fm.is_valid():
                messages.success(request,'form is validates')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm=editadminform(instance=request.user)
                abc = User.objects.all()
            else:
                fm=edituserform(instance=request.user)
                abc=None
        return render(request,'enroll/profile.html',{'form':fm,'name':request.user,'user':abc})
    else:
        return HttpResponseRedirect('/login/')
def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def cpass(request):#change password by entering old password
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user ,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'changes saved successfully')
                print(fm)
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'enroll/cpass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
#change password without entering old password
def cpass2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user ,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'your password has been saved susscefully')
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'enroll/cpass1.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_detail(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=editadminform(instance=pi)
        return render(request,'enroll/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
