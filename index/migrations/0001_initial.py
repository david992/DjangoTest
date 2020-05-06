# Generated by Django 3.0.5 on 2020-04-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adddres', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
    ]