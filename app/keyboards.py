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
        ['Adicionar'],
        ['Remover'],
        ['Editar'],
        ['Listar']
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)


def add_course_again():
    keyboard = [
        ['Adicionar'],
        ['Menu']
    ]

    reply_markup = {}
    reply_markup['keyboard'] = keyboard
    reply_markup['resize_keyboard'] = True
    reply_markup['one_time_keyboard'] = True

    return json.dumps(reply_markup)
