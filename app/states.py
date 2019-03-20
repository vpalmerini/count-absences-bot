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
    }
}