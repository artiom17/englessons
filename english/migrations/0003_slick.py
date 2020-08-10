# Generated by Django 3.0.6 on 2020-06-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0002_auto_20200622_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(upload_to='pics')),
                ('img_1', models.ImageField(upload_to='pics')),
                ('img_2', models.ImageField(upload_to='pics')),
                ('img_3', models.ImageField(upload_to='pics')),
                ('img_4', models.ImageField(upload_to='pics')),
                ('img_5', models.ImageField(upload_to='pics')),
                ('img_6', models.ImageField(upload_to='pics')),
                ('img_7', models.ImageField(upload_to='pics')),
                ('main_title', models.CharField(max_length=200)),
                ('main_text', models.TextField()),
            ],
        ),
    ]
