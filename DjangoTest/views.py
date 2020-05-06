from django.http import HttpResponse


def show_views(request):
    return HttpResponse("my first django")

def show1_views(request,num1):
    return HttpResponse("传递进来的参数为："+str(num1))

def years_view(request,year,mouth,day):
    return HttpResponse("%s年%s月%s日"%(year,mouth,day))
