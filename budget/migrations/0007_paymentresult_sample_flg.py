# Generated by Django 2.0.3 on 2019-06-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_auto_20190609_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentresult',
            name='sample_flg',
            field=models.BooleanField(default=0, verbose_name='サンプルフラグ'),
        ),
    ]
