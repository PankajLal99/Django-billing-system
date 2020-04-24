# Generated by Django 3.0.2 on 2020-02-17 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('invoice', models.IntegerField(primary_key=True, serialize=False)),
                ('seller', models.CharField(max_length=100)),
                ('challan_no', models.IntegerField()),
                ('buyer_order_no', models.IntegerField()),
                ('invoice_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('order_date', models.DateField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('buyer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('rate', models.FloatField()),
                ('unit', models.CharField(max_length=50)),
                ('gst', models.FloatField()),
                ('discount', models.FloatField()),
                ('sub_total', models.FloatField()),
                ('total', models.FloatField()),
                ('words', models.CharField(max_length=100)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Billing')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Buyer')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Products')),
                ('invoice_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Billing')),
            ],
        ),
        migrations.AddField(
            model_name='billing',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Buyer'),
        ),
    ]