# Generated by Django 3.0.7 on 2020-07-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0011_auto_20200705_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtest',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='testtest',
            name='correct_answer_four',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='NO', max_length=255),
        ),
        migrations.AddField(
            model_name='testtest',
            name='correct_answer_one',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='NO', max_length=255),
        ),
        migrations.AddField(
            model_name='testtest',
            name='correct_answer_three',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='NO', max_length=255),
        ),
        migrations.AddField(
            model_name='testtest',
            name='correct_answer_two',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='NO', max_length=255),
        ),
    ]