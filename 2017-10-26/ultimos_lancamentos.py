from requests import get

LINK_API = 'mexi aqui para nao pegar da internet'


def pega_todos_lancamentos_fake():
    return [ i for i in range(0,49) ]


def pega_todos_lancamentos_validos():
    api_resultado = get(LINK_API).json()
    return api_resultado


def qual_foi_o_ultimo():
    api_resultado = pega_todos_lancamentos_validos()
    return api_resultado[-1]


def qual_foi_o_penultimo():
    api_resultado = pega_todos_lancamentos_validos()
    return api_resultado[-2]

def pega_lancamento(n_lancamento):
    api_resultado = pega_todos_lancamentos_validos()
    return api_resultado[n_lancamento - 1]


