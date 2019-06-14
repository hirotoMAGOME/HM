# Generated by Django 2.0.3 on 2019-06-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_paymentresult_sample_flg'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoublePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csrf', models.CharField(max_length=100, verbose_name='csrf')),
                ('post_text', models.CharField(max_length=1000, verbose_name='POST内容')),
                ('create_date', models.DateTimeField(verbose_name='作成日')),
            ],
            options={
                'db_table': 'double_post',
            },
        ),
    ]