from django.urls import path
from . import views

urlpatterns = [
    path('testmain/<int:topic_id>/', views.testmain, name="testmain"),
    path('testphonetics/<int:topic_id>/', views.testphonetics, name="testphonetics"),
    path('homework/<int:topic_id>/', views.homework, name="homework"),
    path('homeworkGrammar/<int:topic_id>/', views.homeworkGrammar, name="homeworkGrammar"),
]
