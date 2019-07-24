from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .froms import UserLoginForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_login_form =UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
                return redirect("article:article_list")
            else:
                return("账号或密码错误,请重新输入")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form':user_login_form}
        return render(request,'userprofile/login.html',context)
    else:
        return HttpResponse("请使用get或者post请求数据")
def user_logout(request):
    logout(request)
    return redirect("article:article_list")
def user_re

