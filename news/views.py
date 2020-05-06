from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
class FourDigitYearConverter:
    regex = '[0-9]{4}'
    def to_python(self, value):
        return int(value)
    def to_url(self, value):
        return '%04d' % value

def index_views(request):
    return HttpResponse("news应用中的index处理视图")

def news_views(request,num1):
    return HttpResponse("传递进来的参数为："+str(num1))

def years_view(request,year,month,day):
    return HttpResponse("%s年%s月%s日"%(year,month,day))
