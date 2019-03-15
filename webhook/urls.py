from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_webhook, name='set_webhook'),
    path('info/', views.get_webhook_info, name='get_webhook_info')
]
