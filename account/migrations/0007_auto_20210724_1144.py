# Generated by Django 3.2.5 on 2021-07-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profilemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='Family',
            field=models.CharField(default=None, max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='Name',
            field=models.CharField(default=None, max_length=100, verbose_name='نام'),
        ),
    ]
