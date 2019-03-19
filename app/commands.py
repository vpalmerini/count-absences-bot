from .models import User
from count_absences_bot.settings import token
from .keyboards import *
from webhook.views import get_url
import requests

def execute_handlers(handlers, message, args):
    f_handlers = handlers.get(message)
    for handler in f_handlers.values():
        function = handler['function']
        arguments = handler['arguments']

        args_list = []
        for arg in arguments:
            args_list.append(args.get(arg)) 
        globals()[function](*args_list)


def store_user(sender):
    user_id = sender['id']
    username = sender['username']
    
    user = User(id=user_id, username=username)
    user.save()


def main_menu(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['reply_markup'] = main_keyboard()
    response['text'] = """
        *Menu Principal*

        *Comandos:*
        /disciplinas - adicione/remova/edite disciplinas
        /ajuda - ajuda luciano
        /codigo - código fonte do bot
    """
    requests.post(get_url('sendMessage'), data=response)


def courses(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['reply_markup'] = courses_keyboard()
    response['text'] = """
        *Disciplinas*

        *Comandos*
        /adicionar - adicione disciplinas
        /remover - remova disciplinas já adicionadas
        /editar - edite disciplinas já adicionadas
        /listar - lista as displinas adicionadas
    """
    requests.post(get_url('sendMessage'), data=response)


def invalid_command(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['text'] = """
        Eu não entendi esse comando :(
    """
    requests.post(get_url('sendMessage'), data=response)
