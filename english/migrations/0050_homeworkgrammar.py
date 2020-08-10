# Generated by Django 3.0.7 on 2020-07-23 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0049_english_topic_text_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWorkGrammar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=200)),
                ('word_1', models.CharField(blank=True, max_length=200)),
                ('semtence_word_one', models.CharField(blank=True, max_length=255)),
                ('complete_semtence_one', models.CharField(blank=True, max_length=255)),
                ('translation_one', models.CharField(blank=True, max_length=255)),
                ('word_2', models.CharField(blank=True, max_length=200)),
                ('semtence_word_two', models.CharField(blank=True, max_length=255)),
                ('semtence_word_two_two', models.CharField(blank=True, max_length=255)),
                ('complete_semtence_two', models.CharField(blank=True, max_length=255)),
                ('translation_two', models.CharField(blank=True, max_length=255)),
                ('word_3', models.CharField(blank=True, max_length=200)),
                ('word_4', models.CharField(blank=True, max_length=200)),
                ('semtence_word_three', models.CharField(blank=True, max_length=255)),
                ('complete_semtence_three', models.CharField(blank=True, max_length=255)),
                ('translation_three', models.CharField(blank=True, max_length=255)),
                ('word_5', models.CharField(blank=True, max_length=200)),
                ('word_6', models.CharField(blank=True, max_length=200)),
                ('semtence_word_four', models.CharField(blank=True, max_length=255)),
                ('complete_semtence_four', models.CharField(blank=True, max_length=255)),
                ('translation_four', models.CharField(blank=True, max_length=255)),
                ('word_7', models.CharField(blank=True, max_length=200)),
                ('word_8', models.CharField(blank=True, max_length=200)),
                ('semtence_word_five', models.CharField(blank=True, max_length=255)),
                ('complete_semtence_five', models.CharField(blank=True, max_length=255)),
                ('translation_five', models.CharField(blank=True, max_length=255)),
                ('scramble_one_one', models.CharField(blank=True, max_length=200)),
                ('scramble_one_two', models.CharField(blank=True, max_length=200)),
                ('scramble_one_three', models.CharField(blank=True, max_length=200)),
                ('scramble_one_four', models.CharField(blank=True, max_length=200)),
                ('scramble_semtence_one', models.CharField(blank=True, max_length=255)),
                ('scramble_two_one', models.CharField(blank=True, max_length=200)),
                ('scramble_two_two', models.CharField(blank=True, max_length=200)),
                ('scramble_two_three', models.CharField(blank=True, max_length=200)),
                ('scramble_two_four', models.CharField(blank=True, max_length=200)),
                ('scramble_semtence_two', models.CharField(blank=True, max_length=255)),
                ('scramble_three_one', models.CharField(blank=True, max_length=200)),
                ('scramble_three_two', models.CharField(blank=True, max_length=200)),
                ('scramble_three_three', models.CharField(blank=True, max_length=200)),
                ('scramble_three_four', models.CharField(blank=True, max_length=200)),
                ('scramble_semtence_three', models.CharField(blank=True, max_length=255)),
                ('scramble_four_one', models.CharField(blank=True, max_length=200)),
                ('scramble_four_two', models.CharField(blank=True, max_length=200)),
                ('scramble_four_three', models.CharField(blank=True, max_length=200)),
                ('scramble_four_four', models.CharField(blank=True, max_length=200)),
                ('scramble_semtence_four', models.CharField(blank=True, max_length=255)),
                ('scramble_five_one', models.CharField(blank=True, max_length=200)),
                ('scramble_five_two', models.CharField(blank=True, max_length=200)),
                ('scramble_five_three', models.CharField(blank=True, max_length=200)),
                ('scramble_five_four', models.CharField(blank=True, max_length=200)),
                ('scramble_semtence_five', models.CharField(blank=True, max_length=255)),
                ('main_sentence_one', models.CharField(blank=True, max_length=250)),
                ('main_sentence_translation_one', models.CharField(blank=True, max_length=250)),
                ('main_sentence_two', models.CharField(blank=True, max_length=250)),
                ('main_sentence_translation_two', models.CharField(blank=True, max_length=250)),
                ('main_sentence_three', models.CharField(blank=True, max_length=250)),
                ('main_sentence_translation_three', models.CharField(blank=True, max_length=250)),
                ('main_sentence_four', models.CharField(blank=True, max_length=250)),
                ('main_sentence_translation_four', models.CharField(blank=True, max_length=250)),
                ('main_sentence_five', models.CharField(blank=True, max_length=250)),
                ('main_sentence_translation_five', models.CharField(blank=True, max_length=250)),
                ('topic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='english.English')),
            ],
        ),
    ]