# Generated by Django 3.2.5 on 2021-07-24 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210724_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='Family',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='Name',
        ),
    ]
