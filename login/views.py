from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#import pyautogui
import os


user = None
# Create your views here.
def login(request):
    # self.error
    error = None
    auth.logout
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    global user
    if request.method == 'POST':

        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']
        #pyautogui.confirm('this is an confirm box')
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            request.session['user'] = user.username
            return redirect('main:main')
        # 존재하지 않는다면
        else:
            error = 'Check your password'
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login/login.html', {'error' : error, "backgroundColor": "#212121", "displayType":"flex"})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request,'login/login.html', {'error':error,"backgroundColor": "#212121", "displayType":"flex"})

def logout(request):
    auth.logout(request)
    return redirect('login:login')
    #return render(request,'login/login.html', {"backgroundColor": "#212121", "displayType":"flex"})

def signup(request):
    return render(request, 'login/Sign-in.html')