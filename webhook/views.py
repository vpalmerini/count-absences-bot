from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from count_absences_bot.settings import token

ngrok_url = 'https://1138de6a.ngrok.io'

# url used as webhook for development stage
url = '{}/{}'.format(ngrok_url, token)

def get_url(method):
    return 'https://api.telegram.org/bot{}/{}'.format(token, method)

@csrf_exempt
def set_webhook(request):
    return HttpResponse(requests.get(get_url('setWebhook'), data={'url':url}))

def get_webhook_info(request):
    return HttpResponse(requests.get(get_url('getWebhookInfo')))
