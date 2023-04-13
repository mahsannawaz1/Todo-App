
from django.shortcuts import render,redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from .form import UserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def userForm(request):
    
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'User Created successfully!')
            return redirect('login')
    else:
        form=UserForm()


    context={
        'form':form
    }
    return render(request,'users/userform.html',context)

@login_required
def userProfile(request):
    return render(request,'users/profile.html')


def userUpdate(request,pk):
   
    if request.method=='POST':
          user_form=UserUpdateForm(request.POST,instance=request.user)
          profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
          if user_form.is_valid()  and  profile_form.is_valid():
             user_form.save()        
             profile_form.save()
             messages.success(request,f'Profile Updated successfully!')
             return redirect('profile')
         
    else:
         user_form=UserUpdateForm(instance=request.user)
         profile_form=ProfileUpdateForm(instance=request.user.profile)
       
    
    context={
        'profileform':profile_form,
        'userform':user_form,
        
    }
    return render(request,'users/userupdate.html',context)