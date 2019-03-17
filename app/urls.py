from django.urls import path, include
from . import views
from count_absences_bot.settings import token

urlpatterns = [
    path(str(token), views.main, name='main'),
]