# Generated by Django 2.1.1 on 2018-09-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20180908_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
    ]
