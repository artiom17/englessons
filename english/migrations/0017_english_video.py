# Generated by Django 3.0.7 on 2020-07-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0016_testtest_lesson_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='english',
            name='video',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]