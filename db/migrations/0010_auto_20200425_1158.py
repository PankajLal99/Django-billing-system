# Generated by Django 3.0.2 on 2020-04-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_auto_20200425_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='buyer',
            field=models.TextField(choices=[('JILA', 'JILA MD UNION TEST ADDREESS \n GST NO : !12343557 \n TESTING'), ('MD', 'MD \n TESTING \n GST : 1234568')]),
        ),
        migrations.AlterField(
            model_name='billing',
            name='status',
            field=models.CharField(choices=[('U', 'UNPAID'), ('P', 'PAID')], max_length=6),
        ),
    ]
