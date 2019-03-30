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

			args = {
				'sender':sender,
                'chat_id':chat_id,
                'input':message
			}

			# if it's the first interaction we instantiate a new chat
			try:
				chat = Chat.objects.get(id=chat_id)
			except:
				chat = Chat(id=chat_id)
				chat.save()

			store_user(sender)
			current_state = chat.state
			next_states = states[current_state]['next_state']
			next_state = next_states.get(message)

			if (next_state):
				# call handlers
				execute_handlers(handlers, message, args)
				# update current state
				chat.state = next_state
				chat.save()
			else:
				# verify if this state accepts an input
				next_state = next_states.get('/input')
				# if it does
				if (next_state):
					handler = states[chat.state]['/input'][next_state]
					execute_handlers(handlers, handler, args)
					# update current state
					chat.state = next_state
					chat.save()
		except Exception as e:
			raise e
			
	
	return HttpResponse(status=200)
