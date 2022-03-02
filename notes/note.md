# 反向解析
>有的时候路由的配置多了会出现非常长的名称，这个时候就可以用**别名**对路由进行代替，这种方式就叫做**反向解析**
## HTML中使用别名
>在前端html页面中，例如form表单的action操作，可以使用反向解析进行路由的跳转，其写法如下：
1. 在urls.py文件中为路由添加name属性，属性值即想要设置的别名
```python
path('post/', views.post, name='post')
```
2. 在html页面的action中对别名进行使用  
注意：action的填写方式为{% url 'name' %}
```html
<form action="{% url 'post' %}" method="...">
    ...
</form>
```
3. 如果在前端中需要用传入参数，则html对应的写法为  
正则匹配中，无名分组反向解析的时候需要传入参数  
```html
<form action="{% url 'post' 2 %}" method="...">
    ...
</form>
```
## 视图中的反向解析
1. 引入reverse模块
```python
from django.urls import reverse
# 用下方方式即可在views中得到别名对应的解析
print(reverse('post'))
```
## 含正则表达式的反向解析
> 如果路由项中包含了正则表达式，反向解析的时候就需要将url中正则表达式传入的参数解析出来。  
> 
> **解析方法**为：为reverse函数添加参数args或kwargs，反向生成对应的路由路径。
1. 假设使用了正则表达式的路由如下：
```python
re_path('register/(\d\d)', views.register, name='register')
```
2. 对应的视图中获取正则表达式的参数
```python
def register(request, param):
    # args接收无名分组的参数，kwargs接收有名分组的参数
    print(reverse('register', args=(param, ))) # args=(param, )写法说是不这样就是传输一个数字，具体啥意思没明白
    return HttpResponse('ok')
```
## 名称空间  
当有多个app时，反向解析会出现识别错app的问题，可以使用名称空间进行对app的区分。可以看django视频的P15  

