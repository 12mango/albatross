# Generated by Django 3.1.7 on 2021-07-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20210703_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='pid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
