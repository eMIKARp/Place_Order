# Generated by Django 2.2.6 on 2019-10-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Place_Order_Application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pnumber',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='pnumber',
            field=models.CharField(max_length=100),
        ),
    ]