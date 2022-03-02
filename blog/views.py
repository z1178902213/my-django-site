# 三大返回常用的方式，render返回一个页面，HttpResponse返回一段HTTP文本，redirect重定向到其他路由
from django.shortcuts import render, HttpResponse, redirect

# 在这里创建项目的视图view，所谓项目视图实际上就是编写函数
from django.urls import reverse
import datetime
from blog.models import User

def index(request):
    list = ['张三', '李四', '王五']
    dic = {'name': '张三', 'age': 16, 'gendar': '男'}
    string = '红红火火恍恍惚惚'
    currentTime = datetime.datetime.now()
    href = '<a href="http://www.baidu.com">百度一下</a>'
    return render(request, 'index.html', locals())

def temp(request):
    return render(request, 'temp.html')

def test1(request, param):
    return HttpResponse(param)


def test2(request, param):
    return HttpResponse(param)


def login(request):
    # get请求参数的获取方式
    # username = request.GET.get('username')
    # password = request.GET.get('password')
    # print(f'用户名：{username}，密码：{password}')

    # post请求参数的获取方式
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(f'用户名：{username}，密码：{password}')

    return render(request, 'login.html')


def post(request):
    return HttpResponse('ok')


def register(request, param):
    # args接收无名分组的参数，kwargs接收有名分组的参数
    print(reverse('register', args=(param,)))
    print(param)
    return HttpResponse(param)


def home(request, y):
    return HttpResponse('home')

def userInfo(request):
    username = request.POST.get('username')
    gender = request.POST.get('gender')
    # 方法一：
    # # 先实例化一个User对象，将对应属性值传入
    # user_obj = models.User(username=username, gender=gender)
    # # 调用对象的save方法将数据保存到数据库中
    # user_obj.save()
    # userQuery = models.User.objects.all()

    # 方法二：
    # models.User.objects.create(username=username, gender=gender)

    # # 批量添加
    # user_list = []
    # user_obj = models.User(username='张三', gender='男')
    # user_list.append(user_obj)
    # user_obj = models.User(username='李四', gender='男')
    # user_list.append(user_obj)
    # user_obj = models.User(username='王五', gender='男')
    # user_list.append(user_obj)
    # models.User.objects.bulk_create(user_list)

    # 条件查询
    # userQuery = models.User.objects.filter(gender='女')

    # # 精确查询-1
    # user_obj = User.objects.filter(uid=10001).first()
    # # 精确查询-2
    # user_obj = User.objects.get(uid=10001)

    # 删除记录
    # delete_info = User.objects.filter(uid__range=[10005, 10010]).delete()
    # print(delete_info)
    user_objs = User.objects.all()
    return render(request, 'userInfo.html', locals())

def addUser(request):
    return render(request, 'addUser.html')