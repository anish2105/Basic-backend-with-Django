# Generated by Django 4.0.1 on 2022-03-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsgo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='details',
            name='views',
            field=models.CharField(max_length=30),
        ),
    ]