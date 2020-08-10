from django.shortcuts import render
from english.models import Phonetics, DictionaryFirst, DictionarySecond, DictionaryThird, MarkPhonetics
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def topic(request, my_id):
    current_user = request.user
    get_mark_info = MarkPhonetics.objects.filter(user_name=current_user, topic_id=my_id)
    topic = Phonetics.objects.get(id=my_id)
    phonetics = Phonetics.objects.all()
    dic_one = DictionaryFirst.objects.get(topic_id=my_id)
    dic_two = DictionarySecond.objects.get(topic_id=my_id)
    dic_three = DictionaryThird.objects.get(topic_id=my_id)
    return render(request, "english/topic.html", {'phonetics': phonetics, 'topic': topic, 'dic_one': dic_one, 'dic_two': dic_two, 'dic_three': dic_three})
