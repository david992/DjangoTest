from django import forms
from .models import *
# 为topic控件初始化数据
topic_choice=(
    ('1','好评'),
    ('2',"中评"),
    ("3","差评"),

)

# 表示评论内容的表单控件
# 控件1---评论标题--文本框
# 控件2---email--email框
# 控件3---内容--Textarea
# 控件4---评论级别--Select
# 控件5---是否保存--Checkbox
class TestForm(forms.Form):
    subject = forms.CharField(label="标题",)
    email = forms.EmailField(label="邮箱")
    #widget=forms.Textarea 将当前属性变成多行文本域
    message = forms.CharField(label="内容",widget=forms.Textarea)
    topic = forms.ChoiceField(label="级别",choices=topic_choice)
    isSaved = forms.BooleanField(label="是否保存")
class  TesterForm(forms.ModelForm):
    class Meta:
        # 指定关联model
        model = Author
        # 指定生成控件的字段
        fields = "__all__"
        # 指定每个控件label
        labels = {
            ' name':'名称',
            'address': "地址",
            'city':"城市",
            'country':'国家',
            'website' :'网址',
        }
        widgets={

        }
