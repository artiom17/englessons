from django.shortcuts import render
from english.models import TestTest, TestPhonetics, Phonetics, HomeWorkPhonetics, HomeWorkGrammar, MarkPhonetics, Mark
from django.contrib.auth.decorators import login_required

from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login')
def testmain(request, topic_id):
    if request.method == 'POST':
        current_user = request.user
        get_mark_info = Mark.objects.filter(user_name=current_user, topic_id=topic_id)
        yes = request.POST.get('yes', None)

        if get_mark_info[0].mark_tests == 0:
            get_mark_info.update(mark_tests=yes)
    test_grammar = TestTest.objects.filter(topic_id=topic_id)
    return render(request, "english/testmain.html", {'test_grammar': test_grammar, 'topic_id': topic_id})


@login_required(login_url='/accounts/login')
def testphonetics(request, topic_id):
    if request.method == 'POST':
        current_user = request.user
        get_mark_info = MarkPhonetics.objects.filter(user_name=current_user, topic_id=topic_id)
        yes = request.POST.get('yes', None)

        if get_mark_info[0].mark_tests == 0:
            get_mark_info.update(mark_tests=yes)

    test_phonetics = TestPhonetics.objects.filter(topic_id=topic_id)
    phonetics = Phonetics.objects.filter(id=topic_id)
    return render(request, "english/testphonetics.html", {'test_phonetics': test_phonetics, 'phonetics': phonetics, 'topic_id': topic_id})


@login_required(login_url='/accounts/login')
def homework(request, topic_id):
    if request.method == 'POST':
        current_user = request.user
        get_mark_info = MarkPhonetics.objects.filter(user_name=current_user, topic_id=topic_id)
        yes = request.POST.get('yes', None)

        if get_mark_info[0].mark_home_work == 0:
            get_mark_info.update(mark_home_work=yes)
    home_work = HomeWorkPhonetics.objects.filter(topic_id=topic_id)
    return render(request, "english/homework.html", {'home_work': home_work, 'topic_id': topic_id})


@login_required(login_url='/accounts/login')
def homeworkGrammar(request, topic_id):
    if request.method == 'POST':
        current_user = request.user
        get_mark_info = Mark.objects.filter(user_name=current_user, topic_id=topic_id)
        yes = request.POST.get('yes', None)

        if get_mark_info[0].mark_home_work == 0:
            get_mark_info.update(mark_home_work=yes)
    home_work_grammar = HomeWorkGrammar.objects.filter(topic_id=topic_id)
    return render(request, "english/homeworkGrammar.html", {'home_work_grammar': home_work_grammar, 'topic_id': topic_id})
