from django.db.models import Avg, Sum
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *


class FourDigitYearConverter:
    regex = '[0-9]{4}'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return '%04d' % value


def index_views1(request,num1):
    return HttpResponse("传递进来的参数为："+str(num1))

def years_view(request,year,month,day):
    return HttpResponse("%s年%s月%s日"%(year,month,day))
def sayhi():
    return "hollo world"
class Dog(object):
    name = "aaaaaaaaaaa"
    def eat(self):
        return "吃狗粮"
def temp_views(request):
    str = "字符串"
    num = 3306
    tup = ("clearlove","jacklove","faker")
    list = ["孙悟空","沙和尚","猪八戒"]
    dic = {
        "BJ":"北京"
    }
    say = sayhi()
    dog =Dog()
    # 通过loader加载模板
    t = loader.get_template("01_temp.html",)
    # 将模板渲染成字符串
    html = t.render(locals())
    # 有HttpResponse将字符串响应给浏览器
    return HttpResponse(html)

def temp1_views(request):
    dic={
        "name":"david",
        "age":"24",
        "gender":"boy"

    }
    # 直接用render函数
    return render(request,'01_temp.html',dic)

def index_views(request):
  return render(request,'index.html')

def login_views(request):
    if request.method == "GET":
        if "uphone" in request.COOKIES:
            return HttpResponse("已登陆过")
        return render(request, 'login.html')
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        if uphone == "david" and upwd == "123456":

            resp = HttpResponse("ok")
            if "isSave" in request.POST:
                resp.set_cookie("uphone", uphone, 60 * 60*24)
            return resp
        else:
            return HttpResponse("失败")
  # return render(request,'login.html')
# def sign_out():
#     if "id" in session and "uname" in session:
#         del session["id"]
#         del session["uname"]
#     return redirect("/index")

def sessioviews(request):
    request.session["uphone"] = 'uphone'
    return HttpResponse("session kok")

def register_views(request):
  return render(request,'register.html')
def addviews(request):
    # Author.objects.create(name="david",age=24,email="24604567@qq.com")
    # Author.objects.create(name="lihui",age=20,email="543212@qq.com")
    # Author.objects.create(name="TYL",age=22,email="54232152@qq.com")

    dic = {
            "title": "诺克萨斯",
            "publicate_date": "2019-10-20",

        }
    obj = Book(**dic)
    obj.save()

    # obj2 =Publisher(name="三峡大学出版社",adddres="三峡",
    #                 city="宜昌",country="湖北",
    #                 website="www.sxdxcbs.com")
    # obj2.save()
    return HttpResponse("add ok ")

def queryviews(request):
    authers = Author.objects.filter(isActive=True)
    print(authers)
    authers1 = Author.objects.all().values()
    authers2 = Author.objects.filter(id=1)
    print(authers2.query)
    print(authers1)
    for i in authers:
        print(i.name,i.age,i.email)
    #     年龄大于22
    AGE = Author.objects.filter(age__gte=22).values()
    # 名字以d开头
    NAME =Author.objects.filter(name__startswith="d")
    print(AGE)
    print(NAME)
    # 不分组聚合函数
    avg = Author.objects.all().aggregate(avg=Avg("age"))
    print(avg)
    # 分组聚合函数
    anno =Author.objects.values("isActive").annotate(sum=Sum("age")).filter(isActive=True).all()
    print(anno)
    odr = Author.objects.order_by("-id")
    print(odr)
    return  render(request,"query_all.html",locals())

def updateviews(request,id):
    author = Author.objects.get(id=id)
    # Author.objects.filter(isActive=False).update(isActive=True)
    if request.method=="GET":
        return render(request, "update.html", locals())
    else:
        name=request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        author.age=age
        author.name=name
        author.email=email
        author.save()
        # return HttpResponse(" update_ok")
        return redirect('/query')

    # return HttpResponse(" ok ")
def deleteviews(request,id):
    author = Author.objects.get(id=id)
    author.isActive=False
    author.save()
    # 使用转发查看query中内容
    # return queryviews(request)
    #重定向
    # return redirect("/query")
    return HttpResponseRedirect("/query")
def authorsviews(request):
    author = Author.objects.all()
    return render(request,'authors.html',locals())

def requestviews(request):
    scheme = request.scheme
    body = request.body
    host=request.get_host()
    path=request.path
    get = request.GET
    post=request.POST
    cookies=request.COOKIES
    print(dir(request))
    return HttpResponse("ok")

def formviews(request):
    if request.method=="GET":
        form = TestForm()
        return render(request,"form.html",locals())
    else:
        # 手动接收数据
        # subject = request.POST['subject']
        # email = request.POST['email']
        # message = request.POST['message']
        # topic = request.POST['topic']
        # isSaved = request.POST['isSaved']
        # print(subject,email,message,topic,isSaved)

        # 自动接收数据
        form = TestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            email= cd['email']
            message= cd['message']
            topic= cd['topic']
            isSaved= cd['isSaved']
        return  HttpResponse(" form_ok")
def  testviews(request):
    if request.method=="GET":
        form = TesterForm()
        return render(request,'test.html',locals())
    else:
        form =TesterForm(request.POST)
        if form.is_valid():
            author = Author(**form.cleaned_data)
            author.save()
        return HttpResponse("OK")

