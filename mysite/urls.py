"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from blog import views


# 这里进行路由配置，path('路由名称', 函数名)
urlpatterns = [
    # path是简单暴力的直接进行匹配的路由，如果需要正则表达使用re_path
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # re_path可以使用正则表达式进行路由匹配，其中\d应该是正则表达式的表示形式，匹配数字的意思
    # 下面这条路由的意思是，index/路由下的任意三个数字组成的路由都可以匹配到对应页面
    # 因此只要知道了正则表达式的写法就可以进行任意方式的路由匹配
    re_path('index/\d\*?', views.index),
    # 如果想要接收正则表达式获取到的参数，用括号将正则表达式包起来，并令路由函数接收参数
    # 不过貌似只能接收到\d对应的参数啊
    re_path('test1/(\d\d\d\d)', views.test1),
    # 上述是无名分组的写法，有名分组可以看下述写法，有名分组对应的参数名称必须相同
    re_path('test2/(?P<param>\d\d)', views.test2),

    # 对路由进行子目录路由，访问blog的时候会跳转到include对应的文件中继续查找路由
    re_path('^blog/', include('blog.urls'))
]
