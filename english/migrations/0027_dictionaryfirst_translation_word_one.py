# Generated by Django 3.0.7 on 2020-07-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0026_auto_20200708_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionaryfirst',
            name='translation_word_one',
            field=models.CharField(default='    -    ', max_length=50),
        ),
    ]
