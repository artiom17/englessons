from django.shortcuts import render
from english.models import English, Phonetics, TestPhonetics, TestTest, Mark, MarkPhonetics
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def lessons(request):
    lessons_all = English.objects.filter().order_by('id')
    phonetics = Phonetics.objects.filter().order_by('id')

    current_user = request.user
    get_mark_info = MarkPhonetics.objects.filter(user_name=current_user)
    get_mark_info_grammar = Mark.objects.filter(user_name=current_user)
    if len(get_mark_info) == 0:
        for i in phonetics:
            add_mark = MarkPhonetics(user_name=current_user, topic_id=i.id)
            add_mark.save()


    if len(get_mark_info_grammar) == 0:
        for i in lessons_all:
            add_mark = Mark(user_name=current_user, topic_id=i.id)
            add_mark.save()

    get_marks_phonetics = MarkPhonetics.objects.filter(user_name=request.user).order_by('topic_id')
    get_marks_grammar = Mark.objects.filter(user_name=request.user).order_by('topic_id')

    num = len(phonetics) + 1
    for i in range(1, num):
        test_phonetics = TestPhonetics.objects.filter(topic_id=i)
        data = Phonetics.objects.filter(id=i).update(length_of_questions=len(test_phonetics))


    num = len(lessons_all) + 1
    for i in range(1, num):
        test_grammar = TestTest.objects.filter(topic_id=i)
        data = English.objects.filter(id=i).update(length_of_questions=len(test_grammar))

    return render(request, "english/lessons.html", {'lessons_all': lessons_all, 'phonetics': phonetics, 'data_phonetics': zip(phonetics, get_marks_phonetics), 'data_grammar': zip(lessons_all, get_marks_grammar)})
