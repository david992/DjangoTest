# Generated by Django 3.0.5 on 2020-04-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_author_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
            options={
                'verbose_name': '夫妻',
                'verbose_name_plural': '夫妻',
                'db_table': 'wife',
            },
        ),
    ]
