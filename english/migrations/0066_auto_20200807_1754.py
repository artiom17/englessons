# Generated by Django 3.0.7 on 2020-08-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0065_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='mark_home_work',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mark',
            name='mark_tests',
            field=models.IntegerField(default=0),
        ),
    ]
