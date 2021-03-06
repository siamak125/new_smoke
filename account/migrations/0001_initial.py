# Generated by Django 3.2.5 on 2021-07-19 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='نام')),
                ('Family', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('Gender', models.IntegerField(choices=[('Man', 'مرد'), ('Woman', 'زن')], verbose_name='جنسیت ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر',
            },
        ),
    ]
