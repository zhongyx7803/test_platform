from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#用来写请求处理逻辑

def login(request):
    """
    用户登录
    """
    return render(request, "login.html")
