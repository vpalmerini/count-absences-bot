from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Chat

@csrf_exempt
def main(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			chat_id = data['message']['chat']['id']

			# if it's the first interaction we instantiate a new chat
			try:
				chat = Chat.objects.get(id=chat_id)
			except:
				chat = Chat(id=chat_id)
				chat.save()
		except Exception as e:
			raise e
			
	
	return HttpResponse(status=200)
