# Generated by Django 3.0.7 on 2020-07-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0062_auto_20200727_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworkgrammar',
            name='speech_sentence_five',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homeworkgrammar',
            name='speech_sentence_four',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homeworkgrammar',
            name='speech_sentence_one',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homeworkgrammar',
            name='speech_sentence_three',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homeworkgrammar',
            name='speech_sentence_two',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]