# Generated by Django 3.0.7 on 2020-08-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0069_english_length_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='slick',
            name='second_parallax_1',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='slick',
            name='second_parallax_2',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='slick',
            name='second_parallax_3',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='slick',
            name='second_parallax_4',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='slick',
            name='second_parallax_5',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='slick',
            name='second_parallax_6',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
    ]