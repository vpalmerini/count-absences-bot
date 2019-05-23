import json

def main_keyboard():
    keyboard = [
        ['Disciplinas'],
        ['Ajuda'],
        ['Código']
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)


def courses_keyboard():
    keyboard = [
        ['Adicionar', 'Remover'],
        ['Editar', 'Listar'],
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)


def add_course_again():
    keyboard = [
        ['Adicionar', 'Menu'],
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)

def remove_course_again():
    keyboard = [
        ['Remover', 'Menu'],
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)


def edit_course_again():
    keyboard = [
        ['Editar', 'Menu'],
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)


def back_menu_keyboard():
    keyboard = [
        ['Menu'],
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time-keyboard'] = True

    return json.dumps(reply_markup)


def edit_course_options_keyboard():
    keyboard = [
        ['Nº de Faltas'],
        ['Sigla'],
        ['Dias e Horários'],
        ['Nº de Créditos'],
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)


def generic_keyboard(queryset_list, field):
    input_list = [element[field] for element in queryset_list]
    keyboard = [input_list[n:n+3] for n in range(0, len(input_list), 3)]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)
