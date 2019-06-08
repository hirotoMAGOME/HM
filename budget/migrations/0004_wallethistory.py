# Generated by Django 2.0.3 on 2019-06-04 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20190522_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0, verbose_name='残高')),
                ('family_id', models.IntegerField(default=0, verbose_name='家族ID')),
                ('member_id', models.IntegerField(default=0, verbose_name='メンバーID')),
                ('create_date', models.DateTimeField(verbose_name='作成日')),
                ('update_date', models.DateTimeField(verbose_name='更新日')),
                ('del_flg', models.BooleanField(default=0, verbose_name='削除フラグ')),
                ('wallet_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budget.Wallet')),
            ],
            options={
                'db_table': 'wallet_history',
            },
        ),
    ]
