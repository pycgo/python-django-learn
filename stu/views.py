from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def index_view(request):
    #return HttpResponse("hello student")
    return render(request, 'login.html')


def login_view(request):
    #接收请求参数  请求是get 写GET方式 post 就写大写的 POST 这样去获取输入的值
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    if uname == 'user01' and pwd == '123456':
        return HttpResponse("登录成功！")
    return HttpResponse("登录失败！！！")


def index_register(request):
    #先判断注册的请求方式
    m = request.method
    if m == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd:
            #创建模型对象 获取输入的用户名 密码  存到数据库
            stu_register = Student(sname=uname, spwd=pwd)
            stu_register.save()

            return HttpResponse("注册成功")
        else:
            return HttpResponse("注册失败")