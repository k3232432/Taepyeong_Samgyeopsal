from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#import pyautogui
import os


# Create your views here.
def main(request):
    return render(request, 'homepage/home.html', {"backgroundColor": "#212121", "displayType":"flex"})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    
def logout(request):
    auth.logout(request)
    return redirect('login:login')
    #return render(request,'login/login.html', {"backgroundColor": "#212121", "displayType":"flex"})



