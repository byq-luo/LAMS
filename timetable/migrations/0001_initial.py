# Generated by Django 2.2.5 on 2019-11-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lab_Number', models.CharField(choices=[('501', '501'), ('507', '507')], max_length=50)),
            ],
            options={
                'verbose_name': 'Timetable',
                'verbose_name_plural': 'Timetables',
            },
        ),
    ]
