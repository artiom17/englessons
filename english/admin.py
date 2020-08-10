from django.contrib import admin
from .models import English, Slick, Phonetics, TestTest, TestPhonetics, DictionaryFirst,\
                    DictionarySecond, DictionaryThird, DictionaryGrammarFirst, DictionaryGrammarSecond,\
                    DictionaryGrammarThird, Customer, Сurriculum, HomeWorkPhonetics, HomeWorkGrammar, Mark, MarkPhonetics


admin.site.register(English)
admin.site.register(TestTest)
admin.site.register(Slick)
admin.site.register(Phonetics)
admin.site.register(TestPhonetics)
admin.site.register(DictionaryFirst)
admin.site.register(DictionarySecond)
admin.site.register(DictionaryThird)
admin.site.register(DictionaryGrammarFirst)
admin.site.register(DictionaryGrammarSecond)
admin.site.register(DictionaryGrammarThird)
admin.site.register(Customer)
admin.site.register(Сurriculum)
admin.site.register(HomeWorkPhonetics)
admin.site.register(HomeWorkGrammar)
admin.site.register(Mark)
admin.site.register(MarkPhonetics)
