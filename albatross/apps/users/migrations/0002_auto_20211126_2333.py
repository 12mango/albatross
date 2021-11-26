# Generated by Django 3.2.9 on 2021-11-26 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userinfo',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='username',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]