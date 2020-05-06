from django.contrib import admin
from .models import *
# Register your models here.
# 高级管理类
class AuthorAdmin(admin.ModelAdmin):
#     指定列表页中显示的字段
    list_display = ["name","age","email",'picture']
# 	列表页上允许显示详情的字段
    list_display_links =("email",'name')
#   详情页中显示的字段及其显示顺序
#   fields = ['name','email','isActive']
#   分组显示的字段
    fieldsets = [
        ('基本信息',{'fields':('name','email'),
                 }
         ),
        ("可选信息",{'fields':('age','isActive','picture'),
                 'classes':('collapse',)
                 }
         )
    ]
#   列表页上允许修改的字段
    list_editable = ("age",)
#   添加允许搜索的字段
    search_fields = ['name','email']
#   添加筛选过滤器
    list_filter = ['name','age']

class BookAdmin(admin.ModelAdmin):
#   时间选择器
    date_hierarchy = 'publicate_date'

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','address','city','website']
    list_editable = ['address','city']
    list_filter = ['address','city']
    search_fields = ['name','website']
    fieldsets = [
        ("基本选项",{'fields':('name','address','city')}),
        ("高级选项",{'fields':('country','website'),'classes':'collapse'})
    ]
class WifeAdmin(admin.ModelAdmin):
    list_display = ['name','age','authors']
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Wife,WifeAdmin)

