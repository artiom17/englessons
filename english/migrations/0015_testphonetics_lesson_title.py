# Generated by Django 3.0.7 on 2020-07-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0014_auto_20200707_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='testphonetics',
            name='lesson_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]