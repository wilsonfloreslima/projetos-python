from time import sleep
from random import randint
def mensagem(msg):
    '''
    -> Mensagem automática.
    :param msg: mesnagem de texto recebido do programa principal
    :return: função não retorna valores
    '''
    print('-'*45)
    print(f' {msg:^}')
    print('-'*45)


def jogo(valor):
    '''
    -> Jogo de advinhação! unção receberá um valor inteiro do programa principal. Sistema vai randomizar um valor entre
        1 e 10 e depois irá compará-los.
    :param valor: valor inteiro do programa principal.
    :return: nao serão retornados valores.
    '''
    while valor < 0 or valor > 10:
        valor = int(input('DADOS INVÁLIDOS! Digite um valor entre 1 e 10: '))
    com = randint(1, 10)
    print('--'*10)
    print('Aguarde...')
    sleep(1)
    print('--'*10)
    print(f'Voce escolheu {valor}')
    print(f'Eu escolhi {com}')
    if valor == com:
        print('\33[32;1mPÁRABENS!!! VOCÊ ACERTOU.\33[m')
    else:
        print('\33[31;1mNÃO ACERTOU! TENTE NOVAMENTE.\33[m')


#programa principal
mensagem("EM QUAL NUMERO ENTRE 1 E 10 ESTOU PENSANDO?")
jog = int(input('Jogador: '))
jogo(jog)
print('--'*10)
print(f'{"FIM DE JOGO!":^20}')