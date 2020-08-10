# Generated by Django 3.0.7 on 2020-08-07 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('english', '0066_auto_20200807_1754'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mark',
            unique_together={('user_name', 'topic')},
        ),
        migrations.CreateModel(
            name='MarkPhonetics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_tests', models.IntegerField(default=0)),
                ('mark_home_work', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='english.English')),
                ('user_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user_name', 'topic')},
            },
        ),
    ]