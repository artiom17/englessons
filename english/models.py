from django.db import models
from django.forms import TextInput, Textarea
from django.contrib.auth.models import User


class English(models.Model):
    lesson_title = models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to="pics", blank=True)
    video_url = models.URLField(blank=True)
    topic_text = models.TextField(blank=True)
    affirmative = models.CharField(max_length=200, blank=True)
    singular = models.TextField(blank=True)
    plural = models.TextField(blank=True)
    interrogative = models.CharField(max_length=200, blank=True)
    singular_question = models.TextField(blank=True)
    plural_question = models.TextField(blank=True)
    negative = models.CharField(max_length=200, blank=True)
    singular_negative = models.TextField(blank=True)
    plural_negative = models.TextField(blank=True)
    topic_text_two = models.TextField(blank=True)

    length_of_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.lesson_title


class TestTest(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(English, on_delete=models.CASCADE, default=None)
    question_num = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
    )
    question_number = models.IntegerField(choices=question_num)
    question = models.TextField()
    answer_one = models.TextField()
    correct_answer_one =  models.BooleanField(default=False)
    answer_two = models.TextField()
    correct_answer_two =  models.BooleanField(default=False)
    answer_three = models.TextField()
    correct_answer_three =  models.BooleanField(default=False)
    answer_four = models.TextField()
    correct_answer_four =  models.BooleanField(default=False)


    def __str__(self):
        return self.lesson_title



class Phonetics(models.Model):
    lesson_title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pics", blank=True)
    video_url = models.URLField(blank=True)
    topic_text = models.TextField(blank=True)
    length_of_questions = models.IntegerField(default=0)
    res_length_of_questions = models.IntegerField(default=0)


    def __str__(self):
        return self.lesson_title


class DictionaryFirst(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(Phonetics, on_delete=models.CASCADE, default=None)
    word_one = models.CharField(max_length=50, blank=True)
    translation_word_one = models.CharField(max_length=50, blank=True)
    word_two = models.CharField(max_length=50, blank=True)
    translation_word_two = models.CharField(max_length=50, blank=True)
    word_three = models.CharField(max_length=50, blank=True)
    translation_word_three = models.CharField(max_length=50, blank=True)
    word_four = models.CharField(max_length=50, blank=True)
    translation_word_four = models.CharField(max_length=50, blank=True)
    word_five = models.CharField(max_length=50, blank=True)
    translation_word_five = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.lesson_title


class DictionarySecond(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(Phonetics, on_delete=models.CASCADE, default=None)
    word_one = models.CharField(max_length=50, blank=True)
    translation_word_one = models.CharField(max_length=50, blank=True)
    word_two = models.CharField(max_length=50, blank=True)
    translation_word_two = models.CharField(max_length=50, blank=True)
    word_three = models.CharField(max_length=50, blank=True)
    translation_word_three = models.CharField(max_length=50, blank=True)
    word_four = models.CharField(max_length=50, blank=True)
    translation_word_four = models.CharField(max_length=50, blank=True)
    word_five = models.CharField(max_length=50, blank=True)
    translation_word_five = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.lesson_title


class DictionaryThird(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(Phonetics, on_delete=models.CASCADE, default=None)
    word_one = models.CharField(max_length=50, blank=True)
    translation_word_one = models.CharField(max_length=50, blank=True)
    word_two = models.CharField(max_length=50, blank=True)
    translation_word_two = models.CharField(max_length=50, blank=True)
    word_three = models.CharField(max_length=50, blank=True)
    translation_word_three = models.CharField(max_length=50, blank=True)
    word_four = models.CharField(max_length=50, blank=True)
    translation_word_four = models.CharField(max_length=50, blank=True)
    word_five = models.CharField(max_length=50, blank=True)
    translation_word_five = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.lesson_title


class DictionaryGrammarFirst(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(English, on_delete=models.CASCADE, default=None)
    word_one = models.CharField(max_length=50)
    translation_word_one = models.CharField(max_length=50)
    word_two = models.CharField(max_length=50)
    translation_word_two = models.CharField(max_length=50)
    word_three = models.CharField(max_length=50)
    translation_word_three = models.CharField(max_length=50)
    word_four = models.CharField(max_length=50)
    translation_word_four = models.CharField(max_length=50)
    word_five = models.CharField(max_length=50)
    translation_word_five = models.CharField(max_length=50)
    word_six = models.CharField(max_length=50, blank=True)
    translation_word_six = models.CharField(max_length=50, blank=True)
    word_seven = models.CharField(max_length=50, blank=True)
    translation_word_seven = models.CharField(max_length=50, blank=True)
    word_eight = models.CharField(max_length=50, blank=True)
    translation_word_eight = models.CharField(max_length=50, blank=True)
    word_nine = models.CharField(max_length=50, blank=True)
    translation_word_nine = models.CharField(max_length=50, blank=True)
    word_ten = models.CharField(max_length=50, blank=True)
    translation_word_ten = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.lesson_title


class DictionaryGrammarSecond(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(English, on_delete=models.CASCADE, default=None)
    word_one = models.CharField(max_length=50)
    translation_word_one = models.CharField(max_length=50)
    word_two = models.CharField(max_length=50)
    translation_word_two = models.CharField(max_length=50)
    word_three = models.CharField(max_length=50)
    translation_word_three = models.CharField(max_length=50)
    word_four = models.CharField(max_length=50)
    translation_word_four = models.CharField(max_length=50)
    word_five = models.CharField(max_length=50)
    translation_word_five = models.CharField(max_length=50)
    word_six = models.CharField(max_length=50, blank=True)
    translation_word_six = models.CharField(max_length=50, blank=True)
    word_seven = models.CharField(max_length=50, blank=True)
    translation_word_seven = models.CharField(max_length=50, blank=True)
    word_eight = models.CharField(max_length=50, blank=True)
    translation_word_eight = models.CharField(max_length=50, blank=True)
    word_nine = models.CharField(max_length=50, blank=True)
    translation_word_nine = models.CharField(max_length=50, blank=True)
    word_ten = models.CharField(max_length=50, blank=True)
    translation_word_ten = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.lesson_title


class DictionaryGrammarThird(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(English, on_delete=models.CASCADE, default=None)
    word_one = models.CharField(max_length=50)
    translation_word_one = models.CharField(max_length=50)
    word_two = models.CharField(max_length=50)
    translation_word_two = models.CharField(max_length=50)
    word_three = models.CharField(max_length=50)
    translation_word_three = models.CharField(max_length=50)
    word_four = models.CharField(max_length=50)
    translation_word_four = models.CharField(max_length=50)
    word_five = models.CharField(max_length=50)
    translation_word_five = models.CharField(max_length=50)
    word_six = models.CharField(max_length=50, blank=True)
    translation_word_six = models.CharField(max_length=50, blank=True)
    word_seven = models.CharField(max_length=50, blank=True)
    translation_word_seven = models.CharField(max_length=50, blank=True)
    word_eight = models.CharField(max_length=50, blank=True)
    translation_word_eight = models.CharField(max_length=50, blank=True)
    word_nine = models.CharField(max_length=50, blank=True)
    translation_word_nine = models.CharField(max_length=50, blank=True)
    word_ten = models.CharField(max_length=50, blank=True)
    translation_word_ten = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.lesson_title


class TestPhonetics(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(Phonetics, on_delete=models.CASCADE, default=None)
    question_num = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
    )
    question_number = models.IntegerField(choices=question_num)
    question = models.TextField()
    answer_one = models.TextField()
    correct_answer_one =  models.BooleanField(default=False)
    answer_two = models.TextField()
    correct_answer_two =  models.BooleanField(default=False)
    answer_three = models.TextField()
    correct_answer_three =  models.BooleanField(default=False)
    answer_four = models.TextField()
    correct_answer_four =  models.BooleanField(default=False)


    def __str__(self):
        return self.lesson_title


class HomeWorkPhonetics(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(Phonetics, on_delete=models.CASCADE, default=None)

    word_1 = models.CharField(max_length=200, blank=True)
    semtence_word_one = models.CharField(max_length=255, blank=True)
    complete_semtence_one = models.CharField(max_length=255, blank=True)
    translation_one = models.CharField(max_length=255, blank=True)

    word_2 = models.CharField(max_length=200, blank=True)
    semtence_word_two = models.CharField(max_length=255, blank=True)
    semtence_word_two_two = models.CharField(max_length=255, blank=True)
    complete_semtence_two = models.CharField(max_length=255, blank=True)
    translation_two = models.CharField(max_length=255, blank=True)

    word_3 = models.CharField(max_length=200, blank=True)
    word_4 = models.CharField(max_length=200, blank=True)
    semtence_word_three = models.CharField(max_length=255, blank=True)
    complete_semtence_three = models.CharField(max_length=255, blank=True)
    translation_three = models.CharField(max_length=255, blank=True)

    word_5 = models.CharField(max_length=200, blank=True)
    word_6 = models.CharField(max_length=200, blank=True)
    semtence_word_four = models.CharField(max_length=255, blank=True)
    complete_semtence_four = models.CharField(max_length=255, blank=True)
    translation_four = models.CharField(max_length=255, blank=True)

    word_7 = models.CharField(max_length=200, blank=True)
    word_8 = models.CharField(max_length=200, blank=True)
    semtence_word_five = models.CharField(max_length=255, blank=True)
    complete_semtence_five = models.CharField(max_length=255, blank=True)
    translation_five = models.CharField(max_length=255, blank=True)

############################################################################################

    scramble_one_one = models.CharField(max_length=200, blank=True)
    scramble_one_two = models.CharField(max_length=200, blank=True)
    scramble_one_three = models.CharField(max_length=200, blank=True)
    scramble_one_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_one = models.CharField(max_length=255, blank=True)

    scramble_two_one = models.CharField(max_length=200, blank=True)
    scramble_two_two = models.CharField(max_length=200, blank=True)
    scramble_two_three = models.CharField(max_length=200, blank=True)
    scramble_two_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_two = models.CharField(max_length=255, blank=True)

    scramble_three_one = models.CharField(max_length=200, blank=True)
    scramble_three_two = models.CharField(max_length=200, blank=True)
    scramble_three_three = models.CharField(max_length=200, blank=True)
    scramble_three_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_three = models.CharField(max_length=255, blank=True)

    scramble_four_one = models.CharField(max_length=200, blank=True)
    scramble_four_two = models.CharField(max_length=200, blank=True)
    scramble_four_three = models.CharField(max_length=200, blank=True)
    scramble_four_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_four = models.CharField(max_length=255, blank=True)

    scramble_five_one = models.CharField(max_length=200, blank=True)
    scramble_five_two = models.CharField(max_length=200, blank=True)
    scramble_five_three = models.CharField(max_length=200, blank=True)
    scramble_five_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_five = models.CharField(max_length=255, blank=True)

############################################################################################

    main_sentence_one = models.CharField(max_length=250, blank=True)
    main_sentence_translation_one = models.CharField(max_length=250, blank=True)

    main_sentence_two = models.CharField(max_length=250, blank=True)
    main_sentence_translation_two = models.CharField(max_length=250, blank=True)

    main_sentence_three = models.CharField(max_length=250, blank=True)
    main_sentence_translation_three = models.CharField(max_length=250, blank=True)

    main_sentence_four = models.CharField(max_length=250, blank=True)
    main_sentence_translation_four = models.CharField(max_length=250, blank=True)

    main_sentence_five = models.CharField(max_length=250, blank=True)
    main_sentence_translation_five = models.CharField(max_length=250, blank=True)

############################################################################################

    speech_sentence_one = models.CharField(max_length=250, blank=True)
    speech_sentence_two = models.CharField(max_length=250, blank=True)
    speech_sentence_three = models.CharField(max_length=250, blank=True)
    speech_sentence_four = models.CharField(max_length=250, blank=True)
    speech_sentence_five = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.lesson_title


class HomeWorkGrammar(models.Model):
    lesson_title = models.CharField(max_length=200)
    topic = models.ForeignKey(English, on_delete=models.CASCADE, default=None)

    word_1 = models.CharField(max_length=200, blank=True)
    semtence_word_one = models.CharField(max_length=255, blank=True)
    complete_semtence_one = models.CharField(max_length=255, blank=True)
    translation_one = models.CharField(max_length=255, blank=True)

    word_2 = models.CharField(max_length=200, blank=True)
    semtence_word_two = models.CharField(max_length=255, blank=True)
    semtence_word_two_two = models.CharField(max_length=255, blank=True)
    complete_semtence_two = models.CharField(max_length=255, blank=True)
    translation_two = models.CharField(max_length=255, blank=True)

    word_3 = models.CharField(max_length=200, blank=True)
    word_4 = models.CharField(max_length=200, blank=True)
    semtence_word_three = models.CharField(max_length=255, blank=True)
    complete_semtence_three = models.CharField(max_length=255, blank=True)
    translation_three = models.CharField(max_length=255, blank=True)

    word_5 = models.CharField(max_length=200, blank=True)
    word_6 = models.CharField(max_length=200, blank=True)
    semtence_word_four = models.CharField(max_length=255, blank=True)
    complete_semtence_four = models.CharField(max_length=255, blank=True)
    translation_four = models.CharField(max_length=255, blank=True)

    word_7 = models.CharField(max_length=200, blank=True)
    word_8 = models.CharField(max_length=200, blank=True)
    semtence_word_five = models.CharField(max_length=255, blank=True)
    complete_semtence_five = models.CharField(max_length=255, blank=True)
    translation_five = models.CharField(max_length=255, blank=True)

############################################################################################

    scramble_one_one = models.CharField(max_length=200, blank=True)
    scramble_one_two = models.CharField(max_length=200, blank=True)
    scramble_one_three = models.CharField(max_length=200, blank=True)
    scramble_one_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_one = models.CharField(max_length=255, blank=True)

    scramble_two_one = models.CharField(max_length=200, blank=True)
    scramble_two_two = models.CharField(max_length=200, blank=True)
    scramble_two_three = models.CharField(max_length=200, blank=True)
    scramble_two_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_two = models.CharField(max_length=255, blank=True)

    scramble_three_one = models.CharField(max_length=200, blank=True)
    scramble_three_two = models.CharField(max_length=200, blank=True)
    scramble_three_three = models.CharField(max_length=200, blank=True)
    scramble_three_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_three = models.CharField(max_length=255, blank=True)

    scramble_four_one = models.CharField(max_length=200, blank=True)
    scramble_four_two = models.CharField(max_length=200, blank=True)
    scramble_four_three = models.CharField(max_length=200, blank=True)
    scramble_four_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_four = models.CharField(max_length=255, blank=True)

    scramble_five_one = models.CharField(max_length=200, blank=True)
    scramble_five_two = models.CharField(max_length=200, blank=True)
    scramble_five_three = models.CharField(max_length=200, blank=True)
    scramble_five_four = models.CharField(max_length=200, blank=True)
    scramble_semtence_five = models.CharField(max_length=255, blank=True)

############################################################################################

    main_sentence_one = models.CharField(max_length=250, blank=True)
    main_sentence_translation_one = models.CharField(max_length=250, blank=True)

    main_sentence_two = models.CharField(max_length=250, blank=True)
    main_sentence_translation_two = models.CharField(max_length=250, blank=True)

    main_sentence_three = models.CharField(max_length=250, blank=True)
    main_sentence_translation_three = models.CharField(max_length=250, blank=True)

    main_sentence_four = models.CharField(max_length=250, blank=True)
    main_sentence_translation_four = models.CharField(max_length=250, blank=True)

    main_sentence_five = models.CharField(max_length=250, blank=True)
    main_sentence_translation_five = models.CharField(max_length=250, blank=True)

############################################################################################

    speech_sentence_one = models.CharField(max_length=250, blank=True)
    speech_sentence_two = models.CharField(max_length=250, blank=True)
    speech_sentence_three = models.CharField(max_length=250, blank=True)
    speech_sentence_four = models.CharField(max_length=250, blank=True)
    speech_sentence_five = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.lesson_title


class Slick(models.Model):
    main_img = models.FileField(upload_to="pics")
    img_1 = models.FileField(upload_to="pics")
    img_2 = models.FileField(upload_to="pics")
    img_3 = models.FileField(upload_to="pics")
    img_4 = models.FileField(upload_to="pics")
    img_5 = models.FileField(upload_to="pics")
    img_6 = models.FileField(upload_to="pics")
    img_7 = models.FileField(upload_to="pics")
    main_title = models.CharField(max_length=100)
    main_title_2 = models.CharField(max_length=100)
    main_text = models.TextField()
    second_parallax_1 = models.FileField(upload_to="pics", blank=True)
    second_parallax_2 = models.FileField(upload_to="pics", blank=True)
    second_parallax_3 = models.FileField(upload_to="pics", blank=True)
    second_parallax_4 = models.FileField(upload_to="pics", blank=True)
    second_parallax_5 = models.FileField(upload_to="pics", blank=True)
    second_parallax_6 = models.FileField(upload_to="pics", blank=True)



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to="pics", blank=True)

    def __str__(self):
        return self.name


class Сurriculum(models.Model):
    title = models.CharField(max_length=100)
    curriculum_text = models.TextField(blank=True)
    start = models.TextField(blank=True)
    question = models.TextField(blank=True)
    notebook = models.TextField(blank=True)
    phonetics = models.TextField(blank=True)
    grammar = models.TextField(blank=True)
    repeat = models.TextField(blank=True)
    words = models.TextField(blank=True)
    radio = models.TextField(blank=True)
    practice = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Mark(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    topic = models.ForeignKey(English, on_delete=models.CASCADE, default=None)
    mark_tests = models.IntegerField(default=0)
    mark_home_work = models.IntegerField(default=0)

    class Meta:
        unique_together = [['user_name', 'topic']]

    def __str__(self):
        return_text = "Пользователь: " + str(self.user_name) + ", Тема: " + str(self.topic) + \
            ", Тесты: " + str(self.mark_tests) + ", Домашняя работа: " + str(self.mark_home_work)
        return return_text


class MarkPhonetics(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    topic = models.ForeignKey(Phonetics, on_delete=models.CASCADE, default=None)
    mark_tests = models.IntegerField(default=0)
    mark_home_work = models.IntegerField(default=0)

    class Meta:
        unique_together = [['user_name', 'topic']]

    def __str__(self):
        return_text = "Пользователь: " + str(self.user_name) + ", Тема: " + str(self.topic) + \
            ", Тесты: " + str(self.mark_tests) + ", Домашняя работа: " + str(self.mark_home_work)
        return return_text
