# Generated by Django 2.0 on 2018-11-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='编程开发', max_length=20, verbose_name='课程类别'),
        ),
    ]