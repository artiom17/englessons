# Generated by Django 3.0.7 on 2020-07-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0056_сurriculum_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='сurriculum',
            name='notebook',
            field=models.TextField(blank=True),
        ),
    ]
