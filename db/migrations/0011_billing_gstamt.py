# Generated by Django 3.0.2 on 2020-04-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20200425_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='gstamt',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
