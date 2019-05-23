from .models import User, Chat, Day, Time, Course
from count_absences_bot.settings import token
from .keyboards import *
from webhook.views import get_url
import requests

def execute_handlers(handlers, message, args):
    f_handlers = handlers.get(message)
    for handler in f_handlers.values():
        function = handler['function']
        print('\nFunction:' + function)
        arguments = handler['arguments']

        args_list = []
        for arg in arguments:
            args_list.append(args.get(arg))
        globals()[function](*args_list)


def store_user(sender):
    user_id = sender['id']
    try:
        username = sender['username']
        user = User(id=user_id, username=username)
    except:
        # user doesn't have username
        user = User(id=user_id)
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

    *Exemplo:* MC102 terça 12h quinta 12h 6

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

    # course initials
    initials = input[0]
    # initials validation
    if (validate_course_initials(initials)):
        course = Course(initials=initials)
        course.save()
        course.user.add(user)

    # course workload
    workload = input[-1]
    # workload validation
    if (validate_course_workload(workload)):
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


def remove_course(sender):
    user_id = sender['id']
    courses = list_courses_as_values(user_id)
    response = {}
    response['chat_id'] = user_id
    response['reply_markup'] = generic_keyboard(courses, 'initials')
    response['parse_mode'] = 'Markdown'
    response['text'] = """
        Atualmente, estas são as disciplinas que vc tem adicionadas
        
        Selecione 1 para removê-la da sua lista de disciplinas
    """

    requests.post(get_url('sendMessage'), data=response)


def delete_course(sender, input):
    user_id = sender['id']
    user = User.objects.get(id=user_id)

    try:
        course = user.courses.get(initials=input)
        course.delete()
    except:
        # to be handled
        print('whatever')
    response = {}
    response['chat_id'] = user_id
    response['reply_markup'] = remove_course_again()
    response['parse_mode'] = 'Markdown'
    response['text'] = """
        *Disciplina removida!*

        Agora vc pode remover outra disciplina ou voltar ao menu inicial
    """

    requests.post(get_url('sendMessage'), data=response)


def list_courses(sender):
    user_id = sender['id']
    user = User.objects.get(id=user_id)

    courses = list(user.courses.values())
    courses_str = [course['initials'] for course in courses]

    response = {}
    response['chat_id'] = user_id
    response['reply_markup'] = back_menu_keyboard()
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    *Estas são as disciplinas que foram adicionadas por vc:*
    {}
    """.format('\n'.join(courses_str))

    requests.post(get_url('sendMessage'), data=response)


def edit_course(sender):
    user_id = sender['id']
    courses = list_courses_as_values(user_id)

    response = {}
    response['chat_id'] = user_id
    response['reply_markup'] = generic_keyboard(courses, 'initials')
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    Estas são as suas disciplinas!
    Selecione uma para editá-la
    """
    requests.post(get_url('sendMessage'), data=response)


def edit_course_selected(sender, input):
    user_id = sender['id']
    user = User.objects.get(id=user_id)
    course = user.courses.get(initials=input)
    print('course initials:' + course.initials)
    chat = Chat.objects.get(id=user_id)
    chat.data = course.initials
    chat.save()
    response = {}
    response['chat_id'] = user_id
    response['reply_markup'] = edit_course_options_keyboard()
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    Selecione o quê você quer editar!
    """
    requests.post(get_url('sendMessage'), data=response)


def edit_number_of_absences(sender):
    user_id = sender['id']
    user = User.objects.get(id=user_id)
    chat = Chat.objects.get(id=user_id)
    course_initials = chat.data
    course = user.courses.get(initials=course_initials)
    absences = course.absences
    response = {}
    response['chat_id'] = user_id
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    O seu número atual de faltas é {}. Digite o número atualizado:
    """.format(str(absences))
    requests.post(get_url('sendMessage'), data=response)


def edit_number_of_absences_handler(sender, input):
    user_id = sender['id']
    user = User.objects.get(id=user_id)
    chat = Chat.objects.get(id=user_id)
    course_initials = chat.data
    course = User.courses.get(initials=course_initials)
    course.absences = input
    course.save()

    response = {}
    response['chat_id'] = user_id
    response['reply_markup'] = edit_course_again()
    response['parse_mode'] = 'Markdown'
    response['text'] = """
    Número de faltas atualizado com sucesso!
    """
    requests.post(get_url('sendMessage'), data=response)


def edit_course_option_selected(sender, input):
    user_id = sender['id']
    user = User.objects.get(id=user_id)
    chat = Chat.objects.get(id=user_id)
    course_initials = chat.data
    course = user.courses.get(initials=course_initials)
    response = {}
    response['chat_id'] = user_id
    response['parse_mode'] = 'Markdown'

    # if (input == 'Nº de Faltas'):
    #     absences = course.absences
    #     text = """O seu número atual de faltas é {}. Digite o número atualizado:""".format(absences)
    #     #  

    # elif (input == 'Sigla'):
    #     initials = course.initials
    #     text = """A sigla atual do desse curso é {}. Digite a sigla atualizada:""".format(initials)

    # elif (input == 'Dias e Horários'):
    #     print('Dias e Horários')

    # elif (input == 'Nº de Créditos'):
    #     workload = course.workload
    #     text = """O número de créditos atual dessa disciplina é {}. Digite o número atualizado:""".format(workload)
    
    # else:
    #     print('Opção Inválida')
    
    response['text'] = text
    requests.post(get_url('sendMessage'), data=response)


def list_courses_as_values(user_id):
    user = User.objects.get(id=user_id)
    return list(user.courses.values())


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
