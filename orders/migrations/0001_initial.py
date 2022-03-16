# Generated by Django 2.1.7 on 2019-04-01 02:23
 
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_price', models.FloatField(default=0)),
                ('o_time', models.DateTimeField(auto_now=True)),
                ('o_status', models.IntegerField(default=0)),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.AXFUser')),
            ],
            options={
                'db_table': 'axf_order',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_goods_num', models.IntegerField(default=1)),
                ('o_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
                ('o_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
            options={
                'db_table': 'axf_ordergoods',
            },
        ),
    ]
