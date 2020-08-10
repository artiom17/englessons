from django.urls import path
from . import views

urlpatterns = [
    path('topic/<int:my_id>/', views.topic, name="topic"),
]
