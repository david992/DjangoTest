# Generated by Django 3.0.5 on 2020-04-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200425_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-age'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='author',
            name='isActive',
            field=models.NullBooleanField(default=True, verbose_name='是否活跃'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]
