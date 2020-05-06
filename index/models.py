from django.db import models

# Create your models here..
class BookManager(models.Manager):
    def title_count(self,key):
        return  self.filter(title_count=key).count()
#     自定义查询年龄小于多少的查询方式
class AuthorManager(models.Manager):
    def age_lt(self,age):
        return self.filter(age_lt=age)
# 创建实体类-Publisher （出版社）
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name="名称")
    address = models.CharField(max_length=200,verbose_name="地址")
    city = models.CharField(max_length=50,verbose_name="城市")
    country = models.CharField(max_length=50,verbose_name="国家")
    website = models.URLField(verbose_name="网址")
    def __str__(self):
        return self.name
    class Meta:
        db_table="publisher"
        verbose_name="出版社"
        verbose_name_plural=verbose_name

class Author(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(null=True,verbose_name="邮箱")
# 增加字段，isActive表示用户及或状态  BoolleaFiled（）
    isActive = models.NullBooleanField(default=True,verbose_name="是否活跃")
    # 用户头像
    picture = models.ImageField(upload_to="static/upload",null=True,
                                verbose_name='头像')
    def __repr__(self):
        return "<Autehor %r>"%self.name

    # 重写__str__方法定义对象的字符串表示
    def __str__(self):
        return self.name
    # 增加内部类Meta定义展现形式
    class Meta:
        # 修改表名
        db_table="author"
        #指定管理时现显示的名字
        verbose_name="作者"
        verbose_name_plural=verbose_name
        # 指定排序规则 年龄降序
        ordering= ["-age"]

class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    authors = models.OneToOneField(Author,on_delete=models.CASCADE,
                                   null=False,verbose_name="对象")

    def __str__(self):
        return self.name
    def __repr__(self):
        return "<Autehor %r>"%self.name

    class Meta:
        db_table="wife"
        verbose_name="夫妻"
        verbose_name_plural=verbose_name
class Book(models.Model):
    objects=BookManager()
    title = models.CharField(max_length=50,verbose_name="书籍")
    publicate_date = models.DateField(verbose_name="出版时间")
    # 一对多 book(多)---publisher(1)
    publisher = models.ForeignKey(Publisher,null=True,
                                  on_delete=models.CASCADE,verbose_name="出版社")
    # 多对多映射添加属性
    authors=models.ManyToManyField(Author,
                                   verbose_name="作者")
    def __str__(self):
        return self.title
    class Meta:
        db_table="book"
        verbose_name="书籍"
        verbose_name_plural=verbose_name