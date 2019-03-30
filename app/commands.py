from .models import User, Day, Time, Course
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
            print(args_list)
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


def add_course_initials(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    *Adicionando Matéria*
        
    O bot precisa das seguintes informações:
    - sigla da disciplina
    - dias e horários de término das aulas
    - nº de créditos

    Primeiro digite a *sigla* da disciplina e pressione *Enviar*

    *Exemplo*
    MC102
    """
    requests.post(get_url('sendMessage'), data=response)


def help_luciano(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    *Ajuda*

    O bot possui os seguintes comandos:
    /disciplinas - adicione/remova/edite/liste disciplinas
    /ajuda - ajuda luciano
    /codigo - código fonte do bot

    Está com algum problema? 
    Tem alguma sugestão de melhoria?
    Entre em contato com @victorpalmerini :)
    """
    requests.post(get_url('sendMessage'), data=response)


def source_code(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    *Código Fonte*

    O código fonte do bot pode ser encontrado em:
    [Repositório](https://github.com/vpalmerini/count-absences-bot)

    Caso queira contribuir está mais do que convidado :)
    E se tiver alguma sugestão de melhoria, entre em contato com @victorpalmerini
    """
    requests.post(get_url('sendMessage'))


def store_course(sender, input):
    user_id = sender['id']
    user = User.objects.get(id=user_id)

    input = (''.join(input)).split()
    print('input:', input)

    # course initials
    initials = input[0]
    # initials validation
    if (validate_course_initials(initials)):
        print('course initials validated')
        course = Course(initials=initials)
        course.save()
        course.user.add(user)

    # course workload
    workload = input[-1]
    # workload validation
    if (validate_course_workload(workload)):
        print('course workload validated')
        course.workload = workload
        course.save()

    # course days and times
    days_times = input[1:-1]
    days = days_times[0:-1:2]
    times = days_times[1::2542997233]

    for day, time in zip(days, times):
        day = Day()
        day.save()
        time = Time()
        time.save()
        time.day.add(day)
        course.day.add(day)

    response = {}
    response['chat_id'] = sender['id']
    response['reply_markup'] = add_course_again()
    response['parse_mode'] = 'Markdown'
    response['text'] = """
        *Disciplina Adicionada!*

        Caso queira adicionar uma nova disciplina:
        /adicionar - adicione novas disciplinas

        Senão, volte para o menu inicial:
        /menu - menu inicial
    """
    requests.post(get_url('sendMessage'), data=response)


def validate_course_initials(initials):
    if (isinstance(initials, str) and len(initials) < 11):
        return True
    else:
        False


def validate_course_workload(workload):
    try:
        workload_int = int(workload)
        return True
    except:
        return False


def invalid_command(chat_id):
    response = {}
    response['chat_id'] = chat_id
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    Eu não entendi esse comando :(
    """
    requests.post(get_url('sendMessage'), data=response)
