# -*- coding: UTF-8 -*-    
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from DjangoVerifyCode import Code
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from PIL import Image
from app01 import comm
from .models  import Admin
from .models  import json
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.template.context_processors import request
from platform import platform
# Create your views here.
def index(req):
    if request.session.get("sess_admin",False):
        return HttpResponseRedirect("admin")
    return comm.render_template(request,"admin/index.html")

def admin(request):
    if not request.session.get("sess_admin",False):
        return HttpResponseRedirect("index")
    system = platform.uname()
    
    res_date ={
    "title":ons.get_version(),
    "diango_version":django.get_version(),
    "system":system[0]+""+system[2],
    }
    return comm.render_template(request, "damin/admin.html", res_data)

def get_code(request):
    ca = comm.Captcha(req)
    ca.type='number'
    ca.img_height=30
    ca.img_width=150
    return ca.display()
def goog_admin_list(request):
    if not request.session.get("sess_admin",False):
        return comm.res_fail(1, "需要登录")
    page =1 
    
    if request.REQUEST.get("page"):
        page=int(request.REQUEST.get("page"))
    page.size=ons.page.size
    
    if request.REQUEST.get("page_size"):
        page.size =int (request.REQUEST.get("page_size"))
    res_date=Admin.getList(page, page_size)
    
    return comm.res_success("请求OK", res_data)

def goog_admin_add(request):
    if not request.session.get("sess_admin",False):
        return comm.res_fail(1, "需要登录")
    name= request.REQUEST.get("name")
    password = request.REQUEST.get("password")
    password2=request.REQUEST.get("password2")
    
    if name =="" :
        return comm.res_fail(1, "必须使用用户名")
    if password =="" :
        return comm.res_fail(1, "请输入密码")
    if password2 ！=pwd2:
        return comm.res_fail(1, "再次输入密码不正确")
    total = Admin.objects.filter(name = name).count()
    if total > 0:
        return commons.res_fail(1, "该用户已存在")
    
    admin = Admin(
        name = name,
        password = pwd,
        add_time = int(time.time())
    )
    admin.save()
    
    return commons.res_success("添加成功", json.loads(admin.toJSON()))
def admin_log(req):
    print req.POST
    username=req.POST.get('username')
    password=req.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(req, user)
        return render_to_response('admin_log.html')
    else:
        return render_to_response('index.html',{'log_err':'用户名密码错误'})
def svn(req):
    if  not req.session.get("sess_admin",False):
        return comm.res_fail(1, "需要登录")
    return render_to_response('svn.html')
    
    