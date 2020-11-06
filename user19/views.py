from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

# Create your views here.
from user19 import models


# user_list =[
#     {"user":"jack", "pwd":"abc"},
#     {"user": "tom", "pwd": "ABC"},
# ]
# 
# 
# def index(request):
# 
#     if request.method == 'POST':
#         username = request.POST.get("username",None)
#         password = request.POST.get("password",None)
# 
#         #添加数据到数据库
#         models.UserInfo.objects.create(user=username,pwd=password)
# 
#         #从数据库中读取所有数据
#         user_list = models.UserInfo.objects.all()
# 
# 
#     return render(request, "index.html",{"data": user_list})
# 


def index(request):
    # pass
    return render(request, 'user19/index.html')


def register(request):
    pass
    return render(request, 'user19/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/user19/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'user19/login.html', {"message": message})

    return render(request, 'user19/login.html')


def logout(request):
    pass
    return redirect('/user19/index/')
