from django.shortcuts import render
from basic_app.form import UserForm,UserProfileform

from basic_app.models import UserProfile
#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):

    return render(request,'home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Acount is not active')
        else:
            print('someone tried and login failed')
            return HttpResponse('invalid login details')

    else:
        return render(request,'login.html',{})

def register(request):
    registered= False

    if request.method == "POST":
        userr=UserForm(data=request.POST)
        profile_form=UserProfileform(data=request.POST)

        if userr.is_valid() and profile_form.is_valid():
            user=userr.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(userr.errors,profile_form.errors)
    else:
        userr = UserForm()
        profile_form = UserProfileform()

    return render(request,'register.html',{
                                           'userr':userr,
                                           'profile_form':profile_form,
                                           'registered':registered})



# Python program to view
# for displaying images
