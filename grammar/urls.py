from django.urls import path
from . import views

urlpatterns = [
    path('grammar/<int:my_id>/', views.grammar, name="grammar"),
]
