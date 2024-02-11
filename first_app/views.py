from django.shortcuts import render,redirect
from .forms import RegisterForm,user_Change_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django import forms
# Create your views here.

# def login(request):

#     return render (request,'login.html')

def sign(request):
    if not request.user.is_authenticated: 
        if request.method =="POST":
            signUp=RegisterForm(request.POST)
            if signUp.is_valid():
               messages.success(request,"Account created successfully")
               signUp.save(commit=True)
               return redirect('sign')
               print(signUp.cleaned_data)

        else:
           signUp=RegisterForm()

        return render (request,'signup.html',{'form':signUp})
    else:
        return redirect('profile')
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
          form = AuthenticationForm(request=request,data=request.POST)
          if form.is_valid():
            name= form.cleaned_data['username']
            userpass= form.cleaned_data['password']
            user = authenticate(username = name,password=userpass)

            if user is not None:
                login(request,user)
                return redirect('profile')
        else:
          form = AuthenticationForm()
       
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')

def profile(request):
    if  request.user.is_authenticated: 
        if request.method =="POST":
            signUp=user_Change_data(request.POST, instance = request.user)
            if signUp.is_valid():
               messages.success(request,"Account updated successfully")
               signUp.save(commit=True)
               return redirect('home')
               print(signUp.cleaned_data)

        else:
           signUp=user_Change_data(instance=request.user)

        return render (request,'profile.html',{'form':signUp})
    else:
        return redirect('sign')
    


def user_logout(request):
   logout(request)
   return redirect('login')


# change password using old password

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
            # messages.success(request,"Password created successfully")
              form.save()
              update_session_auth_hash(request,form.user)
              return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)

    
        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')

def pass_change_2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
            # messages.success(request,"Password created successfully")
              form.save()
              update_session_auth_hash(request,form.user)
              return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)

        return render(request,'passchange.html',{'form':form})
    else:
        return redirect('login')
    


def changeUserdata(request):

    if  request.user.is_authenticated: 
        if request.method =="POST":
            signUp=user_Change_data(request.POST,isinstance=request.user)
            if signUp.is_valid():
               messages.success(request,"Account updated successfully")
               signUp.save(commit=True)
               return redirect('sign')
               print(signUp.cleaned_data)

        else:
           signUp=user_Change_data()

        return render (request,'profile.html',{'form':signUp})
    else:
        return redirect('sign')
