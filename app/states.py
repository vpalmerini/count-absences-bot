states = {
    's0':{
        'next_state':
        {
            '/start':'s1'
        }
    },
    's1':{
        'next_state':
        {
            '/disciplinas':'s2',
            'Disciplinas':'s2',
            '/ajuda':'s3',
            'Ajuda':'s3',
            '/codigo':'s4',
            'Código':'s4'
        }
    },
    's2':{
        'next_state':
        {
            '/adicionar':'s5',
            'Adicionar':'s5',
            '/remover':'s6',
            'Remover':'s6',
            '/editar':'s7',
            'Editar':'s7',
            '/listar':'s8',
            'Listar':'s8'
        }
    },
    's3':{
        'next_state':
        {
            '/menu':'s1',
            'Menu':'s1',
            '/voltar':'s1',
            'Voltar':'s1'
        }
    },
    's4':{
        'next_state':
        {
            '/menu':'s1',
            'Menu':'s1',
            '/voltar':'s1',
            'Voltar':'s1'
        }
    },
    's5':{
        'next_state':
        {
            '/input':'s5.1',
            '/voltar':'s2',
            'Voltar':'s2'
        },
        '/input':{
            's5.1':'/store_course'
        }
    },
    's5.1':{
        'next_state':
        {
            '/adicionar':'s5',
            'Adicionar':'s5',
            '/menu':'s2',
            'Menu':'s2'
        }
    }
}

handlers = {
    '/start':{
        0:{
            'function':'store_user',
            'arguments':['sender']
        },
        1:{
            'function':'main_menu',
            'arguments':['chat_id']
        }
    },
    '/menu':{
        0:{
            'function':'main_menu',
            'arguments':['chat_id']
        }
    },
    'Menu':{
        0:{
            'function':'main_menu',
            'arguments':['chat_id']
        }
    },
    '/ajuda':{
        0:{
            'function':'help_luciano',
            'arguments':['chat_id']
        }

    },
    'Ajuda':{
        0:{
            'function':'help_luciano',
            'arguments':['chat_id']
        }
    },
    '/codigo':{
        0:{ 
            'function':'source_code',
            'arguments':['chat_id']
        }
    },
    'Código':{
        0:{
            'function':'source_code',
            'arguments':['chat_id']
        }
    },
    '/disciplinas':{
        0:{
            'function':'courses',
            'arguments':['chat_id']
        }
    },
    'Disciplinas':{
        0:{
            'function':'courses',
            'arguments':['chat_id']
        }
    },
    '/adicionar':{
        0:{
            'function':'add_course_initials',
            'arguments':['chat_id']
        }
    },
    'Adicionar':{
        0:{
            'function':'add_course_initials',
            'arguments':['chat_id']
        }
    },
    '/store_course':{
        0:{
            'function': 'store_course',
            'arguments': ['sender', 'input']
        }
    }
}