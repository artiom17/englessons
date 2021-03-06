# Generated by Django 3.0.7 on 2020-07-08 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0024_auto_20200708_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictionaryFirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=200)),
                ('word_one', models.CharField(max_length=50)),
                ('word_two', models.CharField(max_length=50)),
                ('word_three', models.CharField(max_length=50)),
                ('word_four', models.CharField(max_length=50)),
                ('word_five', models.CharField(max_length=50)),
                ('word_six', models.CharField(max_length=50)),
                ('word_seven', models.CharField(max_length=50)),
                ('word_eight', models.CharField(max_length=50)),
                ('word_ninne', models.CharField(max_length=50)),
                ('word_ten', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='english.Phonetics')),
            ],
        ),
    ]
