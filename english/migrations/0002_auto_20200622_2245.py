# Generated by Django 3.0.6 on 2020-06-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='english',
            old_name='name',
            new_name='lesson_title',
        ),
        migrations.AddField(
            model_name='english',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='english',
            name='topic_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
