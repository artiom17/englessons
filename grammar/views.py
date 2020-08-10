from django.shortcuts import render
from english.models import English, DictionaryGrammarFirst, DictionaryGrammarSecond, DictionaryGrammarThird, Mark
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def grammar(request, my_id):
    current_user = request.user
    get_mark_info = Mark.objects.filter(user_name=current_user, topic_id=my_id)

    lessons_all = English.objects.get(id=my_id)
    dic_one = DictionaryGrammarFirst.objects.get(topic_id=my_id)
    dic_two = DictionaryGrammarSecond.objects.get(topic_id=my_id)
    dic_three = DictionaryGrammarThird.objects.get(topic_id=my_id)
    return render(request, "english/grammar.html", {'lessons_all': lessons_all, 'dic_one': dic_one, 'dic_two': dic_two, 'dic_three': dic_three})
