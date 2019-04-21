# Generated by Django 2.0.3 on 2019-04-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('sample', models.CharField(max_length=100, null=True, verbose_name='例')),
                ('memo', models.CharField(max_length=100, null=True, verbose_name='備考')),
                ('family_id', models.IntegerField(null=True, verbose_name='家族ID')),
                ('member_id', models.IntegerField(null=True, verbose_name='メンバーID')),
            ],
            options={
                'db_table': 'payment_category',
            },
        ),
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',models.CharField(max_length=20, verbose_name='名前')),

            ],
            options={
                'db_table': 'payment_plan',
            },
        ),
        migrations.CreateModel(
            name='PaymentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_plan_id', models.IntegerField(verbose_name='予算ID')),
                ('amount_plus_flg', models.BooleanField(default=0, verbose_name='収支区分')),
                ('amount', models.IntegerField(verbose_name='金額')),
                ('memo', models.CharField(max_length=100, null=True, verbose_name='備考')),
                ('family_id', models.IntegerField(null=True, verbose_name='家族ID')),
                ('member_id', models.IntegerField(null=True, verbose_name='メンバーID')),
                ('rank', models.IntegerField(null=True, verbose_name='表示順')),
                ('payment_date', models.DateTimeField(verbose_name='支払い日')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('del_flg', models.BooleanField(default=0, verbose_name='削除フラグ')),
            ],
            options={
                'db_table': 'payment_result',
            },
        ),
        migrations.CreateModel(
            name='PaymentUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
            ],
            options={
                'db_table': 'payment_unit',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('wallet_type_id', models.IntegerField(verbose_name='財布種別ID')),
                ('balance', models.IntegerField(verbose_name='残高')),
                ('rank', models.IntegerField(null=True, verbose_name='表示順')),
                ('family_id', models.IntegerField(null=True, verbose_name='家族ID')),
                ('member_id', models.IntegerField(null=True, verbose_name='メンバーID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('del_flg', models.BooleanField(default=0, verbose_name='削除フラグ')),
            ],
            options={
                'db_table': 'wallet',
            },
        ),
        migrations.CreateModel(
            name='WalletType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('family_id', models.IntegerField(null=True, verbose_name='家族ID')),
                ('member_id', models.IntegerField(null=True, verbose_name='メンバーID')),
            ],
            options={
                'db_table': 'wallet_type',
            },
        ),
    ]
