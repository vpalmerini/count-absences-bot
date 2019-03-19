from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat
from .commands import *
from .states import *
import json

@csrf_exempt
def main(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			chat_id = data['message']['chat']['id']
			sender = data['message']['from']
			message = data['message']['text']

			# if it's the first interaction we instantiate a new chat
			try:
				chat = Chat.objects.get(id=chat_id)
			except:
				chat = Chat(id=chat_id)
				chat.save()

			current_state = chat.state
			next_states = states[current_state]['next_state']
			next_state = next_states.get(message)

			args = {
				'sender':sender,
                'chat_id':chat_id,
                'input':message
			}

			if (next_state):
				# call handlers
				execute_handlers(handlers, message, args)
				# update current state
				chat.state = next_state
				chat.save()
			else:
				print('this state doesnt exist yet')
		except Exception as e:
			raise e
			
	
	return HttpResponse(status=200)
