# Generated by Django 2.0.3 on 2019-03-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190324_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='login_id',
            field=models.CharField(default='noname', max_length=20, verbose_name='ログインID'),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default='password', max_length=20, verbose_name='パスワード'),
        ),
    ]