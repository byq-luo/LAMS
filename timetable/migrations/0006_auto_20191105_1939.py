# Generated by Django 2.2.5 on 2019-11-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20191105_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=10, verbose_name='预约人')),
                ('subject', models.CharField(max_length=10, verbose_name='课程名称')),
                ('lab', models.CharField(max_length=10, verbose_name='实验室编号')),
                ('day', models.DateField(verbose_name='预约日期')),
                ('start', models.TimeField(verbose_name='开始时间')),
                ('end', models.TimeField(verbose_name='结束时间')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
            ],
            options={
                'verbose_name': '预约管理',
                'verbose_name_plural': '预约管理',
            },
        ),
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10, verbose_name='实验室编号')),
                ('addr', models.CharField(max_length=10, verbose_name='实验室位置')),
                ('pic', models.ImageField(upload_to='images', verbose_name='实验室照片')),
                ('desc', models.CharField(max_length=50, verbose_name='实验室描述')),
            ],
            options={
                'verbose_name': '实验室管理',
                'verbose_name_plural': '实验室管理',
                'ordering': ['num'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=10, verbose_name='第几周')),
                ('start', models.DateField(verbose_name='起始日期')),
                ('end', models.DateField(verbose_name='结束日期')),
            ],
            options={
                'verbose_name': '学期管理',
                'verbose_name_plural': '学期管理',
                'ordering': ['week'],
            },
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]
